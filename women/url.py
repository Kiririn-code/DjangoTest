from django.urls import path
from .views import *


urlpatterns =[
    path('', index),
    path('cat/<int:catId>/', categories),
]