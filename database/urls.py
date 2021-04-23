from django.urls import path
from database import views

app_name='db'

urlpatterns = [
    path('', views.home, name='db'),
]