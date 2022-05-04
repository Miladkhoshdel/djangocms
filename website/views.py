from audioop import reverse
from .models import WebsiteConfig
from django.shortcuts import redirect, render, resolve_url
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class MainView(TemplateView):
    template_name = "website/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            page_slug = WebsiteConfig.objects.get(key_field='first_page')
            context['name'] = page_slug.value_field.slug
        except WebsiteConfig.DoesNotExist:
            context['name'] = "Please select the first page"
        return context


class NotFound(RedirectView):
    pattern_name = "website:main_url"
    query_string = True
    url = "/"