from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryFrom(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%d/%m/%d',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }