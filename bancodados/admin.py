from django.contrib import admin
from bancodados import models
# Register your models here.

admin.site.register(models.Usuario),
admin.site.register(models.Produto)