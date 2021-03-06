from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class BaseModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="r_owner", verbose_name=_('Owner'))
    create_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    update_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    class Meta:
        abstract = True


class Status(models.IntegerChoices):
    DRAFT = 0, _('Draft')
    PUBLISH = 1, _('Publish')
