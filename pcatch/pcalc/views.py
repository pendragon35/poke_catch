from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from . import calc
from .models import Rates

# Create your views here.
def index(request):
  myrates = Rates.objects.all()
  context = RequestContext(request, {'myrates' : myrates})
  return render(request,'pcalc/index.html',context)

def catch_rate(request):
  myrates = Rates.objects.all()
  context = RequestContext(request, {'myrates' : myrates})
  return render(request,'pcalc/catch_rate.html',context)