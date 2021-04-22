from django.shortcuts import render
from vaderFile import *

# Create your views here.
from django.http import HttpResponse


def index(request):
    sentiment_str = sentiment_scores("is baiha a babys")
    return HttpResponse(sentiment_str)
    # return HttpResponse("Hello world")
