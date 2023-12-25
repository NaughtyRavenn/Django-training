from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    passwd1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    passwd2 = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput())

    def clean_passwd2(self):
        if "passwd1" in self.cleaned_data:
            passwd1 = self.cleaned_data["passwd1"]
            passwd2 = self.cleaned_data["passwd2"]
            if passwd1 == passwd2 and passwd1:
                return passwd2
        raise forms.ValidationError("Mat khau khong hop le")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^\w+$", username):
            raise forms.ValidationError("Ten tai khoan co ki tu dac biet")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tai khoan da ton tai")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["passwd1"],
        )
