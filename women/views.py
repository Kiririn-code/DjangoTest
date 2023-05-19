from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('women')


def categories(request, catId):
    return HttpResponse(f'категория {catId}')
