from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  return HttpResponse("uma questao %s." % question_id)

def results(request, question_id):
  response = "Os resultadoos %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("votando numa questão %s." % question_id)