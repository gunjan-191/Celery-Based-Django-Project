from django.shortcuts import render
from django.http import HttpResponse
from . task import *

# Create your views here.
def index(request):
    handle_sleep.delay()
    return HttpResponse("Hello")
