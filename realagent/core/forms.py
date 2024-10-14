from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from listing.models import UserProfile

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
    profile_type = forms.ChoiceField(
        choices=UserProfile.PROFILE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'block w-full rounded-md border-2 py-1.5 text-gray-900 shadow-sm focus:outline-none focus:ring-2 sm:text-sm sm:leading-6'
        }),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "profile_type")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Check if a UserProfile already exists for this user
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={'profile_type': self.cleaned_data['profile_type']}
            )
            if not created:
                # If profile already exists, update it with the new profile_type
                profile.profile_type = self.cleaned_data['profile_type']
                profile.save()
        return user

    # Styled fields
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))