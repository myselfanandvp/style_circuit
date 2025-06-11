from django.forms import ModelForm
from usermanagement.models import CustomUser



class EditUserForm(ModelForm):
    
    class Meta:
        model=CustomUser
        fields=['email','username','fullname','phonenumber','profile_img','is_superuser','is_active','is_staff']
        exclude=['password','groups','user_permissions']