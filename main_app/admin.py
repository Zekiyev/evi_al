from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import (Region, City, Target, Township, Picture, Metro, CustomUser,
                     Advertisement, Payment, Transaction,)

admin.site.register([Region, City, Target, Township, Picture, Metro, CustomUser, 
                    Advertisement, Payment, Transaction])
