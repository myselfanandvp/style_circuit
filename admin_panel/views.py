from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from usermanagement.models import CustomUser
from .forms import EditUserForm


# Create your views here.

@method_decorator(never_cache, name='dispatch')
class AdminHomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login_url'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, 'notfound.html')

    def get(self, request):
        return render(request, 'admin_views/dashboard.html', {})


@method_decorator(never_cache, name='dispatch')
class AdminListView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login_url'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, 'notfound.html', {})

    def get(self, request):
        users = CustomUser.objects.all()
        if users is not None:
            return render(request, 'admin_views/listuser.html', {'users': users})
        return render(request, 'admin_views/listuser.html', {'users': []})

  

@method_decorator(never_cache, name='dispatch')
class AdminEditView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, 'notfound.html')

    def get(self,request,userid):
        user = CustomUser.objects.get(id=userid)
        form = EditUserForm(instance=user)
        return render(request, 'admin_views/edituser.html', {'form': form})

    def post(self,request,userid):
        user = CustomUser.objects.get(id=userid)
        user = EditUserForm(request.POST,request.FILES, instance=user)
        if user.is_valid():
            user.save()
        return redirect("admin_list_url")


@method_decorator(never_cache, name='dispatch')
class AdminDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, 'notfound')

    def post(self,request,userid):
        CustomUser.objects.get(id=userid).delete()
        return redirect('admin_list_url')
