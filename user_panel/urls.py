from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'user_panel'
urlpatterns = [
     path('index', login_required(views.ProfileView.as_view()), name='profile'),
     path('edit-profile', login_required(views.EditProfileView.as_view()), name='edit_profile'),
     path('change-password', login_required(views.ChangePasswordView.as_view()), name='change_password')

]
