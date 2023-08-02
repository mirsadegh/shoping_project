from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductGallery, ProductCategory, ProductBrand


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    paginate_by = 4
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.filter(status=True, is_delete=False, parent=None)
        context["brands"] = ProductBrand.objects.filter(status=True)
        return context
    
    def get_queryset(self):
        query = super().get_queryset()
        category = self.kwargs.get('cat_id') 
        request = self.request   
        brands = request.GET.get('brands')
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if category is not None:
            query = query.filter(category__id__iexact=category)
        if brands is not None:
            query = query.filter(brand__id__iexact=brands) 
        if start_price:
            query = query.filter(price__gte=start_price)  
        if end_price:
            query = query.filter(price__lte=end_price)          
        return query
    
    
    
class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        context['product_galleries'] = ProductGallery.objects.filter(product_id=loaded_product.id).all()
        return context
  
  
    