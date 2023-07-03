from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'status', 'is_delete']
    list_editable = ['status', 'is_delete', 'category']
    list_filter = ['status', 'is_delete', 'category']
    prepopulated_fields = {'slug': ['title']}


@admin.register(models.ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent', 'is_delete']
    list_editable = ['status', 'is_delete']
    list_filter = ['status', 'is_delete']

@admin.register(models.ProductBrand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_editable = ['status']
    list_filter = ['status']

admin.site.register(models.ProductGallery)


