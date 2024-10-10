from django import forms


class LoginForm(forms.Form):
    """
    Форма Login
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
