from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Never Have I Ever is online!<br><a href='/NHIE/about'>About</a>")    
def about(request):
    return HttpResponse("Never Have I Ever information page!<br><a href='/NHIE/index'>back</a>")
