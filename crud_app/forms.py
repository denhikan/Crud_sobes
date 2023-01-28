from django import forms
from .models import Staff
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'department', 'register_date')
        labels = {'name': 'ФИО сотрудника', 'department': 'Название отдела', 'register_date': 'Время создание записи'}


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите адрес электронной почты'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    telephone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите номер телефона'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'}), error_messages={'required': 'Confirm password'})

    class Meta:
        model = User
        fields = ('username', 'email','telephone' ,'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите свой пароль'}))

    class Meta:
        model = User
        fields = ('email', 'password')
