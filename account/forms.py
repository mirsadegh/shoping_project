from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators


def start_with_0(value):
    if value[0] != '0':
        raise forms.ValidationError("شماره موبایل باید با صفر شروع شود!")


class RegisterForm(forms.Form):
    fullname = forms.CharField(label='نام و نام خانوادگی',
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               validators=[validators.MaxLengthValidator(50)]
                               )
    phone = forms.CharField(label='شماره تلفن',
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.MaxLengthValidator(11), start_with_0])
    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(100),
                    validators.EmailValidator]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(100)]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(100)]

    )
    avatar = forms.ImageField(label='تصویر کاربر',
                              required=False)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password == password:
            return confirm_password
        raise ValidationError('کلمه عبور و تکرار کلمه عبور با هم مغایرت دارند!')


class LoginForm(forms.Form):
    phone = forms.CharField(label='شماره موبایل', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password = forms.CharField(
        label='کلمه عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class OtpLoginForm(forms.Form):
    phone = forms.CharField(label='شماره موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.MaxLengthValidator(11), start_with_0])


class CheckOtpForm(forms.Form):
    code = forms.CharField(label='کد چهار رقمی', widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])
