from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='گذرواژه', widget=forms.PasswordInput)
    password2 = forms.CharField( label='تکرار گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'password', 'is_active', 'is_admin')


def start_with_0(value):
    if value[0] != '0':
        raise forms.ValidationError("شماره موبایل باید با صفر شروع شود!")


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[ validators.MaxLengthValidator(100), validators.EmailValidator,]
        )
    password = forms.CharField(
        label='کلمه عبور', 
        widget=forms.PasswordInput(),
        validators=[ validators.MaxLengthValidator(100)]
        )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[ validators.MaxLengthValidator(100)]

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password == password:
            return confirm_password
        
        return ValidationError('کلمه عبور و تکرار کلمه عبور با هم مغایرت دارند!')


class LoginForm(forms.Form):
    phone = forms.CharField(label='شماره موبایل', widget=forms.TextInput(attrs={
                            'class': 'form-control'}), validators=[validators.MaxLengthValidator(11), start_with_0])
    password = forms.CharField(
        label='کلمه عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class AddressCreationForm(forms.ModelForm):
#     user = forms.IntegerField(required=False)

#     class Meta:
#         model = Address
#         fields = '__all__'


class OtpLoginForm(forms.Form):
    phone = forms.CharField(label='شماره موبایل', widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.MaxLengthValidator(11), start_with_0])
 
    


class CheckOtpForm(forms.Form):
    code = forms.CharField(label='کد چهار رقمی', widget=forms.TextInput(
        attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])
    

