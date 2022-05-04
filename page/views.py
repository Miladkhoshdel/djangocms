from django.shortcuts import render
from .models import Page
from django.views.generic import DetailView
from datetime import datetime


class PageDetailView(DetailView):
    model = Page
    template_name = 'page/details.html'
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['slug'])
        context['now'] = datetime.now()
        return context


