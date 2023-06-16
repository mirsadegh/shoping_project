from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductGallery


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    paginate_by = 4
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        context['product_galleries'] = ProductGallery.objects.filter(product_id=loaded_product.id).all()
        return context
    