from django.urls import path

from . import views

app_name = 'vk_friends'
urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.cities, name='cities')
]
