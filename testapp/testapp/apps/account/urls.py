from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    # post views
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
]