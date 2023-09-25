from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

import base.views
from base.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
