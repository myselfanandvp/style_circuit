from django.urls import path
from .views import SignupView,LoginView,HomeView,LogoutView,ForgotPasswordView,VerifyOtp,ResetPasswordView,ContactView,AboutView,PageNotFound
urlpatterns=[
    path('',LoginView.as_view(),name='login_url'),
    path('signup/',SignupView.as_view(),name='signup_url'),
    path('home/',HomeView.as_view(),name='home_url'),
    path('logout/',LogoutView.as_view(),name='logout_url'),
    path('forgotpassword/',ForgotPasswordView.as_view(),name='forgotpsw_url'),
    path('otp/',VerifyOtp.as_view(),name='otp_url'),
    path('resetpassword/',ResetPasswordView.as_view(),name='resetpsw_url'),
    path('about/',AboutView.as_view(),name="about_url"),
    path("contact/",ContactView.as_view(),name="contact_url"),
    path('notfound/',PageNotFound.as_view(),name='pagenotfound_url')
   
]