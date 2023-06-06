from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'is_delete']
    list_editable = ['status', 'is_delete']
    list_filter = ['status', 'is_delete']

admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.ProductGallery)












