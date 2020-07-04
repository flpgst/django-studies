from django.shortcuts import render
from django.http import HttpResponse
from .models import Aula

# Create your views here.

def index(request):
  class_list = Aula.objects.order_by('-data')
  context = {'class_list': class_list}
  return render(request, 'maratona/index.html', context)

