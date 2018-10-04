from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
                }))
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder': "johnsmith@gmail.com"
                }))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'password must be at least 8 characters with number and alphabets'
                }))
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control'
                
                }))
    


    class Meta:
        model = User
        fields = ('username',
                'email',
                'password1',
                'password2'
                )


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
