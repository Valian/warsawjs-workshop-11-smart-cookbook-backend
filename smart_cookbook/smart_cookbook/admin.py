from django.contrib import admin

from smart_cookbook import models

admin.site.register(models.Recipe)
admin.site.register(models.Ingredient)
