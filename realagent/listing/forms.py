from django import forms
from .models import Listing

INPUT_CLASSES = "block w-full rounded-md border-2 border-[#1d1d1d] py-1.5 text-gray-900 shadow-sm ring-1 ring-[#1d1d1d] placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1d1d1d] sm:text-sm sm:leading-6"
class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'location', 'type', 'title', 'description', 'price', 'thumbnail', 'large')

        widgets = {
                'category': forms.Select(attrs={
                    'class': INPUT_CLASSES
                }),
                'location': forms.Select(attrs={
                    'class': INPUT_CLASSES
                }),
                'type': forms.Select(attrs={
                    'class': INPUT_CLASSES
                }),
                'title': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
            }
class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'type', 'title', 'description', 'price', 'thumbnail', 'large', 'is_sold')

        widgets = {
                    'category': forms.Select(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'location': forms.Select(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'type': forms.Select(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'title': forms.TextInput(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'description': forms.Textarea(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'price': forms.TextInput(attrs={
                        'class': INPUT_CLASSES
                    }),
                    'thumbnail': forms.FileInput(attrs={
                        'class': ''
                    }),
                    'large': forms.FileInput(attrs={
                        'class': ''
                    }),
                }