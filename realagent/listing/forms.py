from django import forms
from .models import Listing

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'location', 'type', 'title', 'description', 'price', 'thumbnail', 'large')

class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'type', 'title', 'description', 'price', 'thumbnail', 'large', 'is_sold')
