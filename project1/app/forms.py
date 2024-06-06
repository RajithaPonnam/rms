# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Request

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class RequestForm(forms.ModelForm):
#     class Meta:
#         model = Request
#         fields = ['requirements', 'phone', 'email']
from django import forms
from .models import Details

class RequestForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['Name', 'Phone', 'Email', 'Location', 'Message']