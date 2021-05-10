from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('current/', views.current, name='current'),
    path('reset_location/', views.reset_location, name='reset'),
]
