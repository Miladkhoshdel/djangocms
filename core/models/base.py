from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    owner = models.CharField(max_length=200, name=_("Owner"))
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_add=True)

