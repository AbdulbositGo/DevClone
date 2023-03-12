from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import Profile, Basic, Coding, Work

text_input_class = 'border border-gray-300 text-black font-semibold text-sm rounded-lg w-full p-2.5 ' \
                   'focus:ring-purple-700 focus:border-purple-700 dark:bg-black dark:border-zinc-700 ' \
                   'dark:placeholder-gray-400 dark:hover:border-zinc-600 dark:text-white'


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
                'class': 'bg-gray-100 rounded focus:ring-purple-700 dark:border-zinc-700 dark:bg-black'
            }),
            'image': forms.FileInput(attrs={
                'class': 'col-span-9 text-sm text-black border border-gray-300 '
                         'rounded-lg cursor-pointer focus:ring-purple-700 focus:border-purple-700 '
                         'dark:text-zinc-600 dark:border-zinc-700 dark:bg-black'
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
