from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse, JsonResponse

class IndexView(View):
    def get(self, request):
        dummy_data = {
            'name': 'Django',
            'type': 'Tool',
            'job': 'Service',
            'age': 5
        }
        return JsonResponse(dummy_data)

    def post(self, request):
        print (request.body)
        #import json
        #data = json.loads(request.body)
        #print (data)
        #data = json.loads(request.body.encode('utf-8'))
        #print (str(data['a']))
        #print (str(data['a']))
        return HttpResponse("Post request")

    def put(self, request):
        print (request.data)
        return HttpResponse("Put request")

    def delete(self, request):
        return HttpResponse("Delete request")
