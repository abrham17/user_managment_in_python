from django.urls import path , include
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('' , views.home , name='home'),
    path('signup/' , views.signup , name='signup'),
    path('login/' , views.login , name='login'),
    path('profile/' , views.profile , name = "profile")
]