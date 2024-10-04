from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from listing.models import Location  # Import the Location model from listing
from .models import Profile

class SignupForm(UserCreationForm):
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),  # Use the available locations from the listing app
        required=True
    )
    account_type = forms.ChoiceField(choices=Profile.ACCOUNT_TYPES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'location', 'account_type')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                location=self.cleaned_data['location'],
                account_type=self.cleaned_data['account_type']
            )
        return user
