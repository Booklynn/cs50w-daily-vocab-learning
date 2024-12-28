from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
        })
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:ring-blue-500 focus:border-blue-500'
            })
