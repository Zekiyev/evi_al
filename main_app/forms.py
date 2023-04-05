from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import NormalUser, CustomUser


class NormalUserCreationForm(UserCreationForm):

    class Meta:
        model = NormalUser
        fields = ("email","phone_number", "user_type", "company_name", 
                  "person_in_charge", "role")



class NormalUserChangeForm(UserChangeForm):

    class Meta:
        model = NormalUser
        fields = ("email","phone_number", "user_type", "company_name", 
                  "person_in_charge", "role")


#class CustomUserCreationForm(UserCreationForm):
#    
#    class Meta:
#        model = CustomUser
#        fields = '__all__'
#
#class CustomUserChangeForm(UserChangeForm):
#    
#    class Meta:
#        model = CustomUser
#        fields = '__all__'