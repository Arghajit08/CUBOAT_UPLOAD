from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('',views.home,name="home"),
    path('result/',views.result,name="result"),
    path('create/', GetView.as_view()),
    
]