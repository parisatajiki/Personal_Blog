from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','show_image')
    list_filter = ('category',)
    list_editable = ('author',)

admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)