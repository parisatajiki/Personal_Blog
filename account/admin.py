from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Profile)

admin.site.site_header = 'مدیریت وبلاگ'
