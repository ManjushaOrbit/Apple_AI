from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path("register/", register, name="register"),
    path('', login, name='login'),
    path("logout", logout_request, name="logout"),
]