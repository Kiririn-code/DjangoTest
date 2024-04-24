
from django.contrib import admin
from django.urls import path
from cachedapplication import views
from women.views import *
from django.urls import include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls, name='redirectName'),
    path('women/', include('women.url')),
    path('sportstore/', include('sportstore.urls')),
    # debug toolbar URLS
    path('__debug__/', include(debug_toolbar.urls)),
    path('home/', views.home, name='home'),
]
handler404 = not_found_error
