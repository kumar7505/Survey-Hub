from django.shortcuts import render, HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)
    # return HttpResponse('<h1>Hello</h1>')