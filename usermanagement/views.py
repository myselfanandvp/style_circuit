import re
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from .forms import SignupForm, LoginForm, ForgotpswForm, OtpForm, RestPasswordForm


# Create your views here.

def reroute(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_home_url')
        else:
            return redirect('home_url')
    return None


@method_decorator(never_cache, name='dispatch')
class SignupView(View):

    def get(self, request):
        redirect_response = reroute(request)
        if redirect_response:
            return redirect_response
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login_url")
        else:
            return render(request, 'signup.html', {'form': form})


@method_decorator(never_cache, name='dispatch')
class LoginView(View):
    def get(self, request):
        redirect_response = reroute(request)
        if redirect_response:
            return redirect_response
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("admin_home_url")
                else:
                    login(request, user)
                    return redirect("home_url")

            else:
                # Valid form, but invalid credentials
                form.add_error(None, "Invalid email or password.")
        # Either form was invalid, or user auth failed
        return render(request, 'login.html', {'form': form})


@method_decorator(never_cache, name='dispatch')
class HomeView(LoginRequiredMixin, View):

    login_url = 'login_url'  
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('admin_home_url')
        return render(request, 'home.html', {})


@method_decorator(never_cache, name='dispatch')
class LogoutView(LoginRequiredMixin, View):
    login_url = 'login_url'

    def post(self, request):
        logout(request)
        return redirect('login_url')


class ForgotPasswordView(View):
    def get(self, request):
        redirect_response = reroute(request)
        if redirect_response:
            return redirect_response
        form = ForgotpswForm()
        return render(request, 'forgotpassword.html', {'form': form})


class VerifyOtp(View):
    def get(self, request):
        redirect_response = reroute(request)
        if redirect_response:
            return redirect_response
        form = OtpForm()
        return render(request, 'verifyotp.html', {'form': form})

    def post(self, request):
        form = OtpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Done")

        return HttpResponse("Failed")


class ResetPasswordView(View):
    def get(self, request):
        redirect_response = reroute(request)
        if redirect_response:
            return redirect_response
        form = RestPasswordForm()
        return render(request, 'resetpassword.html', {'form': form})

    def post(self, request):
        form = RestPasswordForm(request.POST)
        if form.is_valid():
            return HttpResponse('worked')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {})

class PageNotFound(View):
    def get(self,request):
        return render(request,'notfound.html')