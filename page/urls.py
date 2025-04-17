from django.urls import path

from page.views import get_category, create_category, detail_category, delete_category, create_product, \
    detail_pro, delete_pro, product_search_view, update_product
from django.urls import path
from django.contrib.auth import views as auth_views

from page import views

urlpatterns = [
    #auth
    path('0/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    #category crud
    path('', get_category, name = 'category-list'),
    path('create/', create_category, name = 'category-create'),
    path('create/<int:pk>', detail_category, name = 'category-detail'),
    path('delete/<int:pk>', delete_category, name = 'category-delete'),
    #products crud
    path('pro-list/', product_search_view, name = 'product-list'),
    path('pro-create/', create_product, name = 'product-create'),
    path('pro-update/<int:pk>', update_product, name = 'product-update'),
    path('pro-detail/<int:pk>', detail_pro, name = 'product-detail'),
    path('pro-delete/<int:pk>', delete_pro, name = 'product-delete'),
]
