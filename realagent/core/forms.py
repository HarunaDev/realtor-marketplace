from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """
    Form for user login with styled fields.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',  # Placeholder text for the username field
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'  # Tailwind CSS classes for styling
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',  # Placeholder text for the password field
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'  # Tailwind CSS classes for styling
    }))

class SignupForm(UserCreationForm):
    """
    Form for user signup with styled fields.
    """
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # Fields to include in the signup form

    # Create styles for form fields
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',  # Placeholder text for the username field
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'  # Tailwind CSS classes for styling
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',  # Placeholder text for the email field
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'  # Tailwind CSS classes for styling
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',  # Placeholder text for the first password field
        'class': 'w-full py-4 px-6 rounded-xl'  # Tailwind CSS classes for styling
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',  # Placeholder text for the password confirmation field
        'class': 'w-full py-4 px-6 rounded-xl'  # Tailwind CSS classes for styling
    }))
