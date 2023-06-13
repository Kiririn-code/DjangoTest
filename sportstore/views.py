from django.http import *
from django.shortcuts import render, redirect
from .models import *


def StartPage(request):
    return HttpResponse('start page')


def Index(request):
    product = Product.objects.all()
    return render(request, 'sportstore/index.html', {'data': product})


def CreateProduct(request):
    if request.method == 'POST':
        new_product = Product()
        new_product.title = request.POST.get("title")
        new_product.save()
        return redirect(Index)
    else:
        return render(request, 'sportstore/createProduct.html')


def UpdateProduct(request, pkProd):
    product = Product.objects.get(pk=pkProd)
    try:
        if request.method == 'POST':
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.save()
            return redirect(Index)
        else:
            return render(request, "sportstore/updateProduct.html", {"product": product})
    except product.DoesNotExist:
        return HttpResponseNotFound()
