from tabnanny import verbose
from django.db import models
from page.models import Page
from core.models.base import BaseModel
from django.utils.translation import gettext_lazy as _


class WebsiteConfig(BaseModel):
    key_field = models.CharField(_('Key'), max_length=254)
    value_field = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name=_('Value Field'))
    owner = None

    class Meta:
        db_table = "WebsiteConfig"
        verbose_name = _('Website Config')  
        verbose_name_plural = _('Website Configs')  