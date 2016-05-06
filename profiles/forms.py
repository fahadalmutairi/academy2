from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from .models import Comment
from accounts.models import CustomUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']




class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
