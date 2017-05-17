from rest_framework import serializers
from questions.models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'distractors')
