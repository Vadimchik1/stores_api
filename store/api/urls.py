from django.urls import path
from api import views

urlpatterns = [
    # path('stores', views.StoreList.as_view()),
    # path('store/<int:pk>', views.StoreDetail.as_view()),
    # path('<int:store_id>/categories', views.product_categories_list),
    # path('categories/', views.add_product_category),
    # path('category/<int:pk>', views.ProductCategoryDetail.as_view()),
    path('<int:store_id>/categories/<int:category_id>', views.ProductList.as_view()),
    path('<int:store_id>/categories/<int:category_id>/<int:product_id>', views.ProductDetail.as_view()),

]
