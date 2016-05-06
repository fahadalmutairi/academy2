from django import forms
from .models import CustomUser, CustomUserManager
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email", "username")


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
