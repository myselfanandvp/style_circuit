from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from .forms import SignupForm, LoginForm,ForgotpswForm,OtpForm,RestPasswordForm



# Create your views here.

@method_decorator(never_cache, name='dispatch')
class SignupView(View):

    def get(self, request):
        form = SignupForm()
        return render(request, 'signupview.html', {'form': form})

    def post(self, request):
        newuser = SignupForm(request.POST, request.FILES)
        if newuser.is_valid():
            newuser.save()
            return redirect("login_url")
        else:
            return render(request, 'signupview.html', {'form': newuser})


@method_decorator(never_cache, name='dispatch')
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'loginview.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("home_url")
            else:
                # Valid form, but invalid credentials
                form.add_error(None, "Invalid email or password.")
        # Either form was invalid, or user auth failed
        return render(request, 'loginview.html', {'form': form})


@method_decorator(never_cache, name='dispatch')
class HomeView(LoginRequiredMixin, View):

    login_url = 'login_url'

    def get(self, request):
        return render(request, 'homeview.html', {})


class LogoutView(LoginRequiredMixin, View):
    login_url = 'login_url'

    def post(self, request):
        logout(request)
        return redirect('login_url')


class ForgotPasswordView(View):
    def get(self, request):
        form = ForgotpswForm()
        return render(request, 'forgotpassword.html', {'form':form})
    
class VerifyOtp(View):
    def get(self,request):
        form=OtpForm()
        return render(request,'verifyotp.html',{'form':form})
    
    def post(self,request):
        form= OtpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Worked")
        return  HttpResponse("Hello world")
    
    
class ResetPasswordView(View):
    def get(self,request):
        form=RestPasswordForm()
        return render(request,'resetpassword.html',{'form':form})
    
    
    def post(self,request):
        form=RestPasswordForm(request.POST)
        if form.is_valid():
            return HttpResponse("worked")