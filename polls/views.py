from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.shortcuts import render

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#            'latest_question_list': latest_question_list,
#            }
#    return render(request, 'polls/index.html', context)


    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
            }
    return HttpResponse(template.render(context, request))

    #return render(request, 'polls/index.html')

    #print (request)
    #print ("ASDASFASDF")
    #return HttpResponse("Hello, World. You're at the polls index.")

def detail(request, question_id):
    print ("!!!!!")
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on qeustion %s." % question_id)

from polls.models import *
from datetime import datetime
from django.utils import timezone

def query(request, question_id):
    fb = Question(question_text = '####', pub_date = datetime.now()) #timezone.now() + datetime.timedelta(days=30))
    fb.save()

    print ("#####")
    return HttpResponse("SASDFASDF question %s." % question_id)

#def get(request):
#    print ("~~~")
#    return HttpResponse("!!!!!")
#
#def post(request):
#    form = PostForm()
#    print (form)
#    return HttpResponse("asdfasfasdfsdf")
