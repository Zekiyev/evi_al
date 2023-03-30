from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Region, City, Target, Township, Picture, Metro, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


#class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserCreationForm
#    ordering = ['-date_joined']
#
#
#    list_display = ('email', 'phone_number', 'company_name', 'person_in_charge', 'user_type', 'role')
#    list_filter = ('user_type',)
#    search_fields = ('email', 'phone_number', 'company_name', 'person_in_charge', 'user_type', 'role')



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("-date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)