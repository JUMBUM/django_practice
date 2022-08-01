from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    #path('main/', views.main),
    path('show/', views.show),
    path('show2/', views.show2),
    path('show3/', views.show3),
    path('show4/', views.show4),
]