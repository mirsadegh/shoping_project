from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def start_with_0(value):
    if value[0] != '0':
        raise forms.ValidationError("شماره موبایل باید با صفر شروع شود!")


class ChangeProfile(forms.Form):
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
 
    avatar = forms.ImageField(label='تصویر کاربر',
                              required=False,
                              widget=forms.FileInput)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(100)])
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(100)]
       )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password == password:
            return confirm_password 
        raise ValidationError('کلمه عبور و تکرار کلمه عبور با هم مغایرت دارند!')


   

