from django import forms
from .models import Listing

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['category', 'location', 'type', 'title', 'description', 'price', 'thumbnail', 'large']