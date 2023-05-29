from django.shortcuts import render, redirect, reverse
from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User, Otp
from django.contrib import messages
from .decorators import authentication_not_required
from django.utils.decorators import method_decorator
from .forms import LoginForm, OtpLoginForm, CheckOtpForm, RegisterForm
from random import randint
from uuid import uuid4
from django.conf import settings
from datetime import datetime
from datetime import timedelta
import calendar


@method_decorator(authentication_not_required, name='dispatch')
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context)

    def post(self, request):

        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            email = cd.get('email')
            fullname = cd.get('fullname')
            password = cd.get('password')
            avatar = cd.get('avatar')
            phone = cd.get('phone')
            user: bool = User.objects.filter(phone__iexact=phone).exists()
            if user:
                register_form.add_error(
                    'phone', 'شماره وارد شده تکراری میباشد')
            else:
                new_user = User(email=email, fullname=fullname, phone=phone)
                new_user.set_password(password)
                if fullname:
                    new_user.fullname = fullname
                if avatar:
                    new_user.avatar = avatar
                new_user.save()
                login(request, new_user)
                return redirect('/')
            
        return render(request, 'account/register.html', {'register_form': register_form})


@method_decorator(authentication_not_required, name='dispatch')
class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'account/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'کاربر وارد شده پیدا نشد!.')
        else:
            form.add_error('phone', 'کاربر وارد شده معتبر نمیباشد!')
        return render(request, 'account/login.html', {'form': form})


@method_decorator(authentication_not_required, name='dispatch')
class OtpLoginView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/otp_login.html", {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            settings.SMS.verification(
                {'receptor': cd["phone"], 'type': '1', 'template': 'randcode', 'param1': randcode})
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse("account:check_otp") + f'?token={token}')
        else:
            form.add_error('phone', 'شماره وارد شده نامعتبر میباشد!')

        return render(request, 'account/otp_login.html', {'form': form})


@method_decorator(authentication_not_required, name='dispatch')
class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        token = request.GET.get("token")
        otp = Otp.objects.get(token=token)
        gen_time = otp.expiration_date
        current_time = datetime.now()
        current_time_sec = calendar.timegm(current_time.timetuple())
        add_expiration = gen_time + timedelta(minutes=2)
        expiration_second = calendar.timegm(add_expiration.timetuple())

        remaind_time = (expiration_second - current_time_sec)*1000

        return render(request, "account/check_otp.html", {'form': form, 'remaind_time': remaind_time})

    def post(self, request):
        token = request.GET.get("token")

        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            otp = Otp.objects.get(token=token)
            expiration = otp.expiration_date
            add_expiration = expiration + timedelta(minutes=2)
            dt_obj1 = add_expiration.timestamp()
            dt_obj2 = datetime.now().timestamp()
            print(dt_obj1, dt_obj2)
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                if dt_obj1 > dt_obj2:
                    otp = Otp.objects.get(token=token)
                    user, is_create = User.objects.get_or_create(
                        phone=otp.phone)
                    user.set_password('12345678')
                    user.save()
                    login(request, user)
                    otp.delete()
                    return redirect('/')
                else:
                    form.add_error('code', 'زمان ارسال این کد منقضی شده است')
        else:
            form.add_error('phone', 'اطلاعات وارد شده صحیح نمی باشد!')

        return render(request, 'account/check_otp.html', {'form': form})


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home:home'))
