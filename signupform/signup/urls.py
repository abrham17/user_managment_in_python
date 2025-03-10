from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-code/<str:email>/', views.verify_code, name='verify_code'),
    path('update-password/<str:email>/', views.update_password, name='update_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('verify-signup/<str:email>/', views.verify_signup_code, name='verify_signup_code'),

]