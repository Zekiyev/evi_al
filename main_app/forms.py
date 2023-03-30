from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","phone_number", "user_type", "company_name", 
                  "person_in_charge", "role")



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email","phone_number", "user_type", "company_name", 
                  "person_in_charge", "role")
