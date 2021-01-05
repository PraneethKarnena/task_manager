from django.contrib.auth import views as auth_views
from django.urls import path

from core import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]