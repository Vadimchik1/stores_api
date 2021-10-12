from django.urls import path
from api import views

urlpatterns = [
    # path('stores', views.StoreList.as_view()),
    # path('store/<int:pk>', views.StoreDetail.as_view()),
    # path('product_cats', views.CategoryList.as_view()),
    # path('product_cat/<int:pk>', views.CategoryDetail.as_view()),
    path('<int:store_id>/categories/<int:category_id>', views.ProductList.as_view()),
    path('<int:store_id>/categories/<int:category_id>/<int:product_id>', views.ProductDetail.as_view()),
]
