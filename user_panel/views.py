from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ChangeProfile, ChangePasswordForm
from account.models import User
import sweetify


class ProfileView(View):
    def get(self, request):
        return render(request, 'user_panel/my_profile.html')


class EditProfileView(View):
    def get(self, request):
        intial_user = {
            'fullname': request.user.fullname,
            'email': request.user.email,
            'phone': request.user.phone,
            'avatar': request.user.avatar,
        }
        form = ChangeProfile(request.POST or None, initial=intial_user)
        context = {
            'form': form
        }
        return render(request, 'user_panel/edit_profile.html', context)

    # def post(self, request):
    #     form = ChangeProfile(request.POST, request.FILES)
    #     user = User.objects.filter(id=request.user.id).first()
    #     user_fullname = user.fullname
    #     user_email = user.email
    #     user_phone = user.phone

    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         fullname_form = cd.get('fullname')
    #         email_form = cd.get('email')
    #         phone_form = cd.get('phone')
    #         avatar_form = cd.get('avatar')

    #         if fullname_form != user_fullname:
    #             user.fullname = fullname_form

    #         if email_form != user_email:
    #             users_check = User.objects.filter(email__iexact=email_form).exists()
    #             if users_check:
    #                 form.add_error('email', 'ایمیل وارد شده تکراری میباشد!')
    #                 return render(request, 'user_panel/edit_profile.html', {'form': form})
    #             user.email = email_form

    #         if phone_form != user_phone:
    #             users_check = User.objects.filter(phone__iexact=phone_form).exists()
    #             if users_check:
    #                 form.add_error('phone', 'شماره وارد شده تکراری میباشد!')
    #                 return render(request, 'user_panel/edit_profile.html', {'form': form})
    #             user.phone = phone_form
    #             user.phone_active_code = None
    #         if avatar_form:
    #             user.avatar = avatar_form
    #         user.save()
    #         sweetify.success(request, 'اطلاعات مورد نظر با موفقیت برروزرسانی گردید')
    #         return render(request, 'user_panel/my_profile.html')
    #     else:
    #         form.non_field_errors()
    #     return render(request, 'user_panel/edit_profile.html', {'form': form})
    
    def post(self,request):
        form = ChangeProfile(instance=request.user,data=request.POST, files=request.FILES)
        if form.is_valid():     
            form.save()
            sweetify.success(request, 'اطلاعات مورد نظر با موفقیت برروزرسانی گردید')
        else:
            form.non_field_errors()
        return render(request, 'user_panel/edit_profile.html', {'form': form})    
            


class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'user_panel/change_password.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            user.set_password(cd.get('password'))
            user.save()
            sweetify.success(request, 'کلمه عبور با موفقیت بروزرسانی گردید')
            return redirect(reverse('account:login_user')+"?next="+ request.path)
        return render(request , 'user_panel/change_password.html', {'form': form})



