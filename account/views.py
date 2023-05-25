from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
import re
from .decorators import authentication_not_required
from django.utils.decorators import method_decorator



@method_decorator(authentication_not_required, name='dispatch')
class LoginUser(View): 
	def get(self, request):
		form = LoginForm()
		context = {'form' : form}
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
	



class LogoutUser(View):
	def get(self, request):
		logout(request)
		return redirect(reverse('home:home'))


