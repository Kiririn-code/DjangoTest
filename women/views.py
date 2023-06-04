from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'women/index.html', {'title': 'ass'})


def categories(request, catId):
    if catId >= 10:
        return redirect('redirectName', permanent=True)
    if catId == 5:
        raise Http404()
    return HttpResponse(f'категория {catId}')


def post(request, postId):
    return HttpResponse(f'post - {postId}')


def not_found_error(request, exception):
    return HttpResponseNotFound(f'ошибка')
