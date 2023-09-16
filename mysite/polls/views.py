from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { 
               "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def whatever(request):
    return HttpResponse("this is the page at 'whatever'?")


def detail(request, question_id):
    return HttpResponse(f"Do f strings work for looking at variables, such as a question? {question_id}")


def results(request, question_id):
    response = "This is a weird format for this, but here is your question: %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("not trying an f string here - question: %s." % question_id)

