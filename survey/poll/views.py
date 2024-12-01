from django.shortcuts import render, HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
    return render(request, 'poll/index.html')
    # return HttpResponse('<h1>Hello</h1>')