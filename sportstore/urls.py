from django.urls import path
from sportstore.views import *

urlpatterns = [

    path('index/', Index, name="index"),
    path('update/<int:pkProd>/', UpdateProduct, name='update'),
    path('create/', CreateProduct, name='create'),
    path('', StartPage),
]
