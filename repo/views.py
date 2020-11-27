from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse

from django.template import loader
from .models import PerfFile
from django.shortcuts import render

class UpdateView(View):
    def get(self, request):
        #latest_perf_file_list = PerfFile.objects.order_by('-pub_date')[:50]
        #context = {
        #        'latest_perf_file_list': latest_perf_file_list,
        #        }
        #return render(request, 'repo/index.html', context)

        dummy_data = {
            'name': 'HistoryDB',
            'type': 'Repo',
            'job': 'Service'
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


def index(request):
    latest_perf_file_list = PerfFile.objects.order_by('-pub_date')[:50]
    context = {
            'latest_perf_file_list': latest_perf_file_list,
            }
    return render(request, 'repo/index.html', context)

#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#            'latest_question_list': latest_question_list,
#            }
#    return HttpResponse(template.render(context, request))

from repo.models import *
from datetime import datetime
import json
from django.forms.models import model_to_dict

def query(request, perf_file_id):
    obj = PerfFile.objects.get(pk = perf_file_id)
    print (model_to_dict(obj))

    return JsonResponse(model_to_dict(obj))

    #all_entries = PerfFile.objects.all()
    #print (model_to_dict(all_entries[0]))

    #fb = PerfFile(name = '####', perf_data = json.dumps('{"a":"b"}'), pub_date = datetime.now())
    ##fb = PerfFile(name = '####', pub_date = datetime.now())
    #fb.save()

    #return HttpResponse("SASDFASDF question %s." % perf_file_id)

