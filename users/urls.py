from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('register', views.register),
    path('userlogin', views.userlogin),
    path('userlogout', views.userlogout),
    path('newblog', views.newblog),
]
