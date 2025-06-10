from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from usermanagement.models import CustomUser

# Create your views here.

@method_decorator(never_cache,name='dispatch')
class AdminHomeView(LoginRequiredMixin,View):
    login_url='login_url'
    def get(self,request):
        return render(request,'admin_views/home.html',{})
    
@method_decorator(never_cache,name='dispatch')
class AdminListView(LoginRequiredMixin,View):
    login_url='login_url'
    def get(self,request):
        users = CustomUser.objects.all()
        if users is not None:            
            return render(request,'admin_views/listuser.html',{'users':users})
        return render(request,'admin_views/listuser.html',{'users':[]})
        