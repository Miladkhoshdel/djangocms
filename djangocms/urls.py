from django.contrib import admin
from django.urls import path, include
from . import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('page.urls', namespace='page')),
]
