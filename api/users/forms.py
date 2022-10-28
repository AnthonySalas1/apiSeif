from django import forms

from api.users.models import User


class UserForm(forms.ModelForm):
    passwd = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
