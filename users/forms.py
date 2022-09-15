from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="First Name", required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter First Name...'}))
    last_name = forms.CharField(max_length=100, label="Last Name", required=True, 
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name...'}))
    email = forms.EmailField(max_length=100, required=True, 
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address...'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    # Since the username, password1, and password2 fields are pre-built-in to the framework, this function is required for me to be able to customize those fields to my likings
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Enter Username...'})                                                                                                            
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password...'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'})
        self.fields['password2'].label = "Password Confirmation"

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="First Name", required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter First Name...'}))
    last_name = forms.CharField(max_length=100, label="Last Name", required=True, 
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name...'}))
    email = forms.EmailField(max_length=100, required=True, 
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address...'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    # Since the username, password1, and password2 fields are pre-built-in to the framework, this function is required for me to be able to customize those fields to my likings
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Enter Username...'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone']