from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register-user', views.RegisterView.as_view(), name='register_user'),
    path('login-user', views.LoginUser.as_view(), name='login_user'),
    path('login-otp', views.OtpLoginView.as_view(), name= 'login_otp'),
    path('check-otp', views.CheckOtpView.as_view(), name= 'check_otp'),
    path('logout-user', views.LogoutUser.as_view(), name='logout_user'),

]






