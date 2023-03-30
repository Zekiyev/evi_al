from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group, AbstractUser
from django.utils import timezone

from .managers import CustomUserManager
from .constants import (ADVERTISEMENT_TYPE_CHOICES, #ADVERTISEMENT_SUB_TYPE_CHOICES, 
                          BUILDING_TYPE_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES, 
                          ADMIN_CONFIRMATION_STATUS_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES,
                          USER_TYPE_CHOICES, BUILDING_PROJECT_TYPE_CHOICES, 
                          PAYMENT_STATUS_CHOICES, TRANSACTION_OPERATION_CHOICES)


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        db_table = 'City'

   
class Region(models.Model):
    name = models.CharField(max_length=255)
    city_for_rel = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
        
    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table = 'Region'
 

class Township(models.Model):
    name = models.CharField("Township", max_length=255)
    region_for_rel = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'Township'


class Metro(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
 
    class Meta:
        db_table = 'Metro'

    
class Target(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table = 'Target'
        
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    company_name = models.CharField("company", max_length=255,null=True,blank=True)
    person_in_charge = models.CharField("person_in_charge",max_length=255)
    phone_number = models.CharField("phone_number", max_length=255,unique=True)
    user_type = models.BigIntegerField(choices=USER_TYPE_CHOICES,default=4)
    role = models.TextField("role",null=True,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "User"


class Advertisement(models.Model):
    room_count = models.BigIntegerField(blank=True, null=True)    
    area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                               help_text='Sahə, m² ilə göstərilmişdir')

    area_of_land = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                       help_text='Torpaq sahəsi, sot ilə göstərilmişdir')

    coast = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text='Torpaq sahəsi, sot ilə göstərilmişdir')

    location_width = models.DecimalField(max_digits=10, decimal_places=7, blank=True, 
                                        null=True, help_text='Longitude')
    
    location_height = models.DecimalField(max_digits=10, decimal_places=7, blank=True, 
                                          null=True, help_text='Latitude')
    type = models.BigIntegerField(choices=ADVERTISEMENT_TYPE_CHOICES)
    #sub_type = models.BigIntegerField(choices=?)
    have_government_deed = models.BooleanField(blank=True, null=True)
    have_mortgage_support = models.BooleanField(blank=True, null=True)
    building_stage_height = models.BigIntegerField(blank=True, null=True)
    stage = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    view_count = models.BigIntegerField(blank=True,null=True)
    advertisement_create_date = models.DateTimeField(blank=True, null=True)
    advertisement_expire_date = models.DateTimeField(blank=True, null=True)
    advertisement_deleted_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    town_ship = models.ForeignKey('Township', on_delete=models.CASCADE)    
    metro = models.ForeignKey('Metro', on_delete=models.CASCADE)
    target = models.ForeignKey('Target', on_delete=models.CASCADE)
    repair = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    building_type = models.BigIntegerField(choices=BUILDING_TYPE_CHOICES)
    admin_confirmation_status = models.BigIntegerField(default=1, 
                                                       choices=ADMIN_CONFIRMATION_STATUS_CHOICES)

    advertisement_type = models.BigIntegerField(choices=ADVERTISEMENT_VIP_TYPE_CHOICES)
    advertisement_type_expire_date = models.DateTimeField(null=True, blank=True)
    building_project_type = models.BigIntegerField(choices=BUILDING_PROJECT_TYPE_CHOICES,
                                                   default=3)

    class Meta:
        db_table = 'Advertisement'
        
        
class Picture(models.Model):
    url = models.CharField(max_length=255)
    advertisement = models.ForeignKey('Advertisement', on_delete=models.CASCADE)
    deleted_date = models.DateTimeField()
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'Picture'    
    
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BigIntegerField(choices=PAYMENT_STATUS_CHOICES)
    order_id = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.email, self.amount)

    class Meta:
        db_table = 'Payment'        

class Transaction(models.Model):
    start_balance = models.DecimalField(max_digits=10, decimal_places=2)#null=True
    end_balance = models.DecimalField(max_digits=10, decimal_places=2)#null=True
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    operation = models.PositiveIntegerField(choices=TRANSACTION_OPERATION_CHOICES)
    order_id = models.CharField(max_length=255)     #null=True
    session_id = models.CharField(max_length=255)   #null=True
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} - {}'.format(self.operation, self.amount)
    
    class Meta:
        db_table = 'Transaction'