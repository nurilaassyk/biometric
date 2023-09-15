from django.db import models

from api.validators import IINValidator, iin_validate


class People(models.Model):
    iin = models.CharField(null=False, blank=False, verbose_name='IIN', max_length=12, unique=True,
                           validators=[IINValidator, iin_validate])
