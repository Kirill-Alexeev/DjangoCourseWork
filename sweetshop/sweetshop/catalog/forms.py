from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'table__input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'table__input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'table__input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'table__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'table__input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'table__input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class OrderForm(forms.ModelForm):
    execution_date = forms.DateField(label='Дата выполнения', widget=forms.DateInput(attrs={'class': 'table__input'}))
    comment = forms.CharField(label='Комментарий к заказу', widget=forms.TextInput(attrs={'class': 'table__input'}))
    delivery_address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'table__input'}))

    class Meta:
        model = Order
        fields = ['execution_date', 'comment', 'delivery_address']
    