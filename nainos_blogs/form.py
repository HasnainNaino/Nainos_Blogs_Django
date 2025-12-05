from django import forms
from .models import Comment

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '   Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' Enter Your Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' type your comment here...'}), 
        }