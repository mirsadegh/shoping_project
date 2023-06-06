from django.urls import path
from . import views



app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('detail-product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
]
