from django.urls import path, include
from . import views

app_name = 'detection'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log, name='login'),

]
