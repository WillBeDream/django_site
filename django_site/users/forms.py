from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class OurRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2" ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email" ] 

class ProfileAvatar(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ["avatar"]



