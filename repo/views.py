from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader
from .models import PerfFile
from django.shortcuts import render

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

def query(request, perf_file_id):
    fb = PerfFile(name = '####', perf_data = json.dumps('{"a":"b"}'), pub_date = datetime.now())
    #fb = PerfFile(name = '####', pub_date = datetime.now())
    fb.save()

    return HttpResponse("SASDFASDF question %s." % perf_file_id)

