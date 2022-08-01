from django.urls import path
from . import views

urlpatterns = [
    path('cart_list/', views.view_Cart_List),
        path('cart_list2/', views.view_Cart_List2),
]
