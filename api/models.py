from django.db import models


class People(models.Model):
    iin = models.CharField(null=False, blank=False, verbose_name='IIN', max_length=12, unique=True)



