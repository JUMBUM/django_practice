from django.urls import path
from . import views

urlpatterns = [
    path('test2/', views.show),
    path('test1/', views.show1),
    path('test3/', views.show2),
]
