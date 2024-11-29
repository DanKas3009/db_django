from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.getProductsList.as_view(), name='getProductsList'),
    path('product/<str:productcode>/', views.getProduct.as_view(), name='getProduct'),
]