from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@method_decorator(never_cache,name='dispatch')
class AdminHomeView(LoginRequiredMixin,View):
    login_url='login_url'
    def get(self,request):
        return render(request,'admin_views/home.html',{})