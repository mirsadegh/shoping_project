from django.urls import path, re_path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('cat/<cat_id>', views.ProductListView.as_view(), name='product_cat_list'),
    path('filter/', views.ProductListView.as_view(), name='product_filter'),
    re_path(r'detail-product/(?P<slug>[-\w]+)', views.ProductDetailView.as_view(), name='product_detail'),
]



