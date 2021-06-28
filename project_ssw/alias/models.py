from django.db import models


class Alias(models.Model):
    alias = models.CharField(max_length=24)
    target = models.CharField(max_length=24)
    start = models.DateTimeField()
    end = models.DateTimeField(default=None, null=True)
