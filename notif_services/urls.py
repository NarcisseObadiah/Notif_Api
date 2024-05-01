from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receive_notification/', views.receive_notification, name='receive_notification'),
]
