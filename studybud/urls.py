from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

import base.views
from base.views import home

def home(request):
    return HttpResponse('Hello, World!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
