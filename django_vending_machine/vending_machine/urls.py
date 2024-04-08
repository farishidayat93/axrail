from django.urls import path
from . import views

urlpatterns = [
     # base page urls
     path('', views.vending_machine_view, name='home'),
     path('vending_machine/<str:category>/', views.vending_machine_view, name='home'),
     path('pay_item/', views.vending_machine_actions, name='home'),
]