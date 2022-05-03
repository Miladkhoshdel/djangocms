from audioop import reverse
import django
from django.shortcuts import redirect, render, resolve_url
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class MainView(TemplateView):
    template_name = "website/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Milad"
        return context


class NotFound(RedirectView):
    pattern_name = "website:main_url"
    query_string = True
    url = "/"