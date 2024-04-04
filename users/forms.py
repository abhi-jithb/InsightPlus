from django import forms
from .models import UserRegistrationModel

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), 
        max_length=100,
        required=True
    )
    loginid = forms.CharField(
        widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), 
        max_length=100,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', 'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
        max_length=100,
        required=True
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}'}), 
        max_length=100,
        required=True
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}), 
        max_length=100,
        required=True
    )
    locality = forms.CharField(
        widget=forms.TextInput(),
        max_length=100,
        required=True
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 22}), 
        max_length=250,
        required=True
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), 
        max_length=100,
        required=True
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), 
        max_length=100,
        required=True
    )
    status = forms.CharField(
        widget=forms.HiddenInput(), 
        initial='waiting', 
        max_length=100
    )

    class Meta:
        model = UserRegistrationModel
        fields = '__all__'
