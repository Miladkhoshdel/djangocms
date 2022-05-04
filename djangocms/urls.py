from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from website.views import NotFound
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls', namespace='page')),
    path('', include('website.urls', namespace='Website')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = NotFound.as_view()