from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def acknowledgement(request):
    print ("!@#!@!@#")
    return render(request,'main/acknowledgement.html')

