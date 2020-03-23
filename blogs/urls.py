from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<str:slug>', views.indexlatest),
    path('blog/', views.blog),
    path('search/', views.search),
    path('blog/<str:slug>', views.blogpost, name='blogpost'),
]
