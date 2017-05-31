import csv
from rest_framework import viewsets, views
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from questions.models import Question
from questions.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = None

@method_decorator(csrf_exempt, name='dispatch')
class QuestionsCsvView(views.APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        overwrite = request.POST.get('overwrite', 'Missing')
        if overwrite not in ['overwrite', 'append']:
            return self.error_http_response(400,
                'invalid overwrite value: "' + overwrite + '"')

        print("Receiving file (to " + overwrite + ")...")
        client_file = request.FILES['csvFile']
        filename = '/tmp/joel-qs-csv-upload'
        with open(filename, 'wb+') as temp_file:
            for chunk in client_file.chunks():
                temp_file.write(chunk)
        print("Received file")

        # Decode the data before updating DB in case data contains error(s)
        csv_data, error_msg = self.read_csv(filename)
        if error_msg:
            return self.error_http_response(400, error_msg)
        print("Parsed CSV")

        # CSV data is valid; update database
        return self.update_db(overwrite, csv_data)

    def read_csv(self, filename):
        parsed_csv = []
        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile, delimiter='|')
            for row in csvreader:
                if row[0].lower() == 'question':
                    continue
                if len(row) != 3:
                    return None, "invalid row: " + "|".join(row)
                parsed_csv.append(row)
            return parsed_csv, None

    def update_db(self, overwrite, parsed_data):
        if overwrite == 'overwrite':
            Question.objects.all().delete()

        # Insert multiple questions into the DB at a time to speed this up
        CHUNK_SIZE=500
        for chunk in self.chunks(parsed_data, CHUNK_SIZE):
            Question.objects.bulk_create(self.lists_to_question_objs(chunk))

        return HttpResponse("OK")

    def lists_to_question_objs(self, lists):
        return map(
            lambda l: Question(question=l[0], answer=l[1], distractors=l[2]),
            lists
        )

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l. (From StackOverflow.)"""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def error_http_response(self, status, reason):
        context = {
            'status': str(status),
            'reason': reason,
        }
        response = HttpResponse(json.dumps(context),
            content_type='application/json')
        response.status_code = 400
        return response
