from django.contrib import admin
from .models import WebsiteConfig

@admin.register(WebsiteConfig)
class WebsiteConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'key_field', 'value_field')
