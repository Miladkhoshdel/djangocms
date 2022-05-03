from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from website.views import NotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls', namespace='page')),
    path('', include('website.urls', namespace='Website')),
]

handler404 = NotFound.as_view()