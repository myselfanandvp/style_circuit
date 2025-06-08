from django.urls import path
from .views import SignupView,LoginView,HomeView,LogoutView,ForgotPasswordView,VerifyOtp,ResetPasswordView
urlpatterns=[
    path('signup/',SignupView.as_view(),name='signup_url'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('home/',HomeView.as_view(),name='home_url'),
    path('logout/',LogoutView.as_view(),name='logout_url'),
    path('forgotpassword/',ForgotPasswordView.as_view(),name='forgotpsw_url'),
    path('otp/',VerifyOtp.as_view(),name='otp_url'),
    path('resetpassword/',ResetPasswordView.as_view(),name='resetpsw_url'),
]