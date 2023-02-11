from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import Profile, Basic, Coding, Work

text_input_class = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 ' \
                   'focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 ' \
                   'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': text_input_class}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': text_input_class}))

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': text_input_class}),
            'email': forms.EmailInput(attrs={'class': text_input_class}),
        }


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': text_input_class}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': text_input_class}))


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'display_email', 'first_name', 'last_name', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': text_input_class}),
            'last_name': forms.TextInput(attrs={'class': text_input_class}),
            'email': forms.EmailInput(attrs={'class': text_input_class}),
            'display_email': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 '
                         'rounded focus:ring-blue-500 '
                         'dark:focus:ring-blue-600 dark:ring-offset-gray-800 '
                         'focus:ring-2 dark:bg-gray-700 dark:border-gray-600'
            }),
            'image': forms.FileInput(attrs={
                'class': 'block w-full col-span-9 text-sm text-gray-900 border '
                         'border-gray-300 rounded-lg cursor-pointer bg-gray-50 '
                         'dark:text-gray-400 focus:outline-none dark:bg-gray-700 '
                         'dark:border-gray-600 dark:placeholder-gray-400'
            }),
        }


class BasicModelForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ['site', 'location', 'bio']
        widgets = {
            'site': forms.TextInput(attrs={'class': text_input_class}),
            'location': forms.TextInput(attrs={'class': text_input_class}),
            'bio': forms.TextInput(attrs={'class': text_input_class})
        }


class CodingModelForm(forms.ModelForm):
    class Meta:
        model = Coding
        fields = ['current', 'skills']
        widgets = {
            'current': forms.TextInput(attrs={'class': text_input_class}),
            'skills': forms.TextInput(attrs={'class': text_input_class}),
        }


class WorkModelForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['work', 'education']
        widgets = {
            'work': forms.TextInput(attrs={'class': text_input_class}),
            'education': forms.TextInput(attrs={'class': text_input_class}),
        }
