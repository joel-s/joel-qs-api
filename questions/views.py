from rest_framework import viewsets, views
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from questions.models import Question
from questions.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = None

@method_decorator(csrf_exempt, name='dispatch')
class QuestionsCSVView(views.View):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        print("Receiving file...")
        my_file = request.FILES['csvFile']
        filename = '/tmp/joel-qs-csv-upload'
        with open(filename, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)
        print("Received file")
        # my_saved_file = open(filename)
        return HttpResponseRedirect("/")
