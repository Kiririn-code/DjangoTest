from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('women')


def categories(request, catId):
    if catId >= 10:
        return redirect('redirectName', permanent=True)
    if catId == 5:
        raise Http404()
    return HttpResponse(f'категория {catId}')


def notFoundError(request, exception):
    return HttpResponseNotFound(f'ошибка')
