from django.db import models
from core.models.base import BaseModel, Status
from core.utils.upload import upload_path
from django.utils.translation import gettext_lazy as _


class Page(BaseModel):
    title = models.CharField(_('Title'), max_length=255)
    sub_title = models.CharField(_('Sub Title'), max_length=255)
    slug = models.SlugField()
    body = models.TextField(_('Body'))
    image = models.ImageField(_('Image'), upload_to=upload_path)
    status = models.SmallIntegerField(_('Status'), choices=Status.choices, default=Status.DRAFT)
    meta_description = models.CharField(_('Meta Description'), max_length=160)
    meta_keyword = models.CharField(_('Meta Keyword'), max_length=160)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Page"
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
