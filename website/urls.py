from django.urls import path
from .views import MainView, NotFound

app_name = 'website'

urlpatterns = [
    path('notfound/', NotFound.as_view(), name="not_found"),
    path('', MainView.as_view(), name="main_url"),
]