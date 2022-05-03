from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    owner = models.CharField(_("Owner"), max_length=200)
    create_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    update_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    class Meta:
        abstract = True


class Status(models.IntegerChoices):
    DRAFT = 0, _('Draft')
    PUBLISH = 1, _('Publish')
