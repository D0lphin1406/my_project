from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpRequest
from . import urls

def about_me(request):
    return render(request, 'my_resume/resume.html')