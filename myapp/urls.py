
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('check/<input>/', views.check),
    path('api/<input>/', views.api),
    path('info/', views.pc_info),
]
