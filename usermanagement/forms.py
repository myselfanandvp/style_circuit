from django.forms import ModelForm
from .models import CustomUser
from django import forms

class SignupForm(ModelForm):
    input_field_style= {'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}
    email=forms.EmailField(widget=forms.EmailInput(attrs={**input_field_style}))
    username=forms.CharField(widget=forms.TextInput(attrs=input_field_style),label="User Name")
    fullname=forms.CharField(widget=forms.TextInput(attrs=input_field_style),label='Full Name')
    phonenumber=forms.CharField(widget=forms.NumberInput(attrs={**input_field_style,'placeholder':'1234567895'}),max_length=10,label="Phone Number")
    password=forms.CharField(widget=forms.PasswordInput(attrs=input_field_style),label="Password")
    profile_img=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-pointer'}),label='Profile Image')
    class Meta:
        model = CustomUser
        fields = ['email','username','fullname','phonenumber','password','profile_img']
        exclude=['first_name','last_name','is_active','is_staff','is_superuser','last_login','groups','user_permissions','date_joined']
        
    def save(self,commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    input_field_style= {'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}
    email=forms.EmailField(widget=forms.EmailInput(attrs={**input_field_style}),required=True,label="Email")
    password=forms.CharField(widget=forms.PasswordInput(attrs=input_field_style),required=True,label="Password")
    
    


class ForgotpswForm(forms.Form):
    input_field_style= {'class':'bg-blue-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}
    email=forms.EmailField(widget=forms.EmailInput(attrs={**input_field_style}))
    
    
class OtpForm(forms.Form):
    otp_field=forms.CharField(widget=forms.NumberInput(attrs={'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-2'}),label="OTP:")

            
    
