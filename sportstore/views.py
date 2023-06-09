from django.http import *
from django.shortcuts import render
from .models import *


def StartPage(request):
    return HttpResponse('start page')


def Index(request):
    product = Product.objects.all()
    return render(request, 'index', {'data': product})


def CreateProduct(request):
    if request.method == 'POST':
        new_product = Product()
        new_product.title = request.POST.get("title")
    return HttpResponseRedirect("/")


def UpdateProduct(request, pkProd):
    product = Product.objects.get(pk=pkProd)
    try:
        if request.method == 'POST':
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "update", {"product": product})
    except product.DoesNotExist:
        return HttpResponseNotFound()
