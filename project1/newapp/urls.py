from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services_view, name='services'),
    path('about/', views.about_view, name='about'),    
    path('', views.run_view, name='home'),
    path('products/', views.product_list, name='product'),
]