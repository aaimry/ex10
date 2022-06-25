from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "phone",)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "phone",
        )
