from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login-user', views.LoginUser.as_view(), name='login_user'),
    path('logout-user', views.LogoutUser.as_view(), name='logout_user'),
]

