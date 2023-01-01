from django.urls import path
from . import views


app_name = 'web'
urlpatterns = [
        path('', views.loginPage, name='loginPage'),
        path('registerPage/<str:pk>', views.registerPage, name='registerPage'),
        path('registerData', views.registerData, name='registerData'),
        path('loginUser', views.loginUser, name='loginUser'),
    ]