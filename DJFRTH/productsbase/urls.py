from django.urls import path
from .views import (product_detail_view, product_create_view, product_delete_view, product_dfs_view)

app_name = 'productsbase'
urlpatterns = [
    path('dfs/<int:my_id>/', product_dfs_view, name='my_dfs'),
    path('product/', product_detail_view, name='product'),
    path('create/', product_create_view),
    path('product/<int:my_id>/delete/', product_delete_view, name='product_delete'),
]