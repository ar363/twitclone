from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import Tweet

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class TweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture', 'bio']
    
    def clean_profile_picture(self):
        pfp = self.cleaned_data.get('profile_picture', False)
        if pfp:
            if pfp._size > 0.25*1024*1024:
                raise ValidationError("Image file too large ( > 250kb )")
            return pfp
        else:
            return None
