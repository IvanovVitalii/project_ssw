from django.contrib import admin
from django.contrib.admin import ModelAdmin

from alias.models import Alias


@admin.register(Alias)
class AdminAlias(ModelAdmin):
    pass
