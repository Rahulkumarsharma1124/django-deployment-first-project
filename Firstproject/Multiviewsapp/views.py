from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Good morning-have a nice day </h2> <hr />");
    
def f2(request):
    return HttpResponse("<h2>Good afternoon-have u done lunch </h2> <hr />");
    
def f3(request):
    return HttpResponse("<h2>good evening</h2> <hr />");
    
