from django.urls import path
from api import views

urlpatterns = [
    path('stores', views.StoreList.as_view()),
    path('store/<int:pk>', views.StoreDetail.as_view()),
    path('<int:store_id>/categories', views.product_categories_list),
    path('categories/', views.add_product_category),

    # path('<int:store_id>/category/', views.ProductCategoryList.as_view()),
]
