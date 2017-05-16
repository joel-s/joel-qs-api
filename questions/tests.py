import json
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from questions.models import Question
from questions.serializers import QuestionSerializer


# Some of this code is based on
# https://github.com/erdem/DRF-TDD-example/blob/master/todoapp/todos/tests.py


class QuestionTestCase(APITestCase):
    url = "/questions"

    def setUp(self):
        pass

    def test_create_question(self):
        response = self.client.post(self.url, make_typical_question(1))
        self.assertEqual(201, response.status_code)

    def test_get_questions(self):
        """
        Test to verify user questions list
        """
        Question.objects.create(**make_typical_question(1))
        Question.objects.create(**make_typical_question(2))

        response = self.client.get(self.url)
        self.assertEqual(len(json.loads(response.content.decode())),
                         Question.objects.count())


class QuestionDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.question = Question.objects.create(
            question="Who ate my pudding?",
            answer="Nobody",
            distractors="Goldilocks, Papa Bear, Mama Bear"
        )
        self.url = "/questions/" + str(self.question.id)

    def test_question_object_bundle(self):
        """
        Test to verify question object bundle
        """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        serializer_data = QuestionSerializer(instance=self.question).data
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_question_object_update(self):
        response = self.client.put(self.url, make_typical_question(7))
        response_data = json.loads(response.content.decode())
        question = Question.objects.get(id=self.question.id)
        self.assertEqual(response_data.get("answer"), "9")


def make_typical_question(num):
    answer = num + 2
    distractors = " ,".join((str(answer - 1), str(answer + 1), str(answer + 2)))
    return {
        'question': "What's " + str(num) + " + 2?",
        'answer': str(answer),
        'distractors': distractors,
    }
