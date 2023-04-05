from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, Permission, 
                                        Group,)
from django.utils import timezone

from .managers import CustomUserManager
from .constants import (ADVERTISEMENT_TYPE_CHOICES, #ADVERTISEMENT_SUB_TYPE_CHOICES, 
                          BUILDING_TYPE_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES, 
                          ADMIN_CONFIRMATION_STATUS_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES,
                          USER_TYPE_CHOICES, BUILDING_PROJECT_TYPE_CHOICES, 
                          PAYMENT_STATUS_CHOICES, TRANSACTION_OPERATION_CHOICES,
                          ADVERTISEMENT_SUB_TYPE_CHOICES)


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Şəhər')
    
    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        verbose_name = 'Şəhər'
        verbose_name_plural = 'Şəhərlər'
        db_table = 'cities'

   
class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name='Rayon')
    city_id = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE,
                                db_constraint=False)
        
    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table = 'regions'
        verbose_name = 'Rayon'
        verbose_name_plural = 'Rayonlar'
 

class Township(models.Model):
    name = models.CharField(verbose_name="Qəsəbə", max_length=255)
    region_id = models.ForeignKey(Region, null=True, blank=True, 
                                  on_delete=models.CASCADE, db_constraint=False)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'townships'
        verbose_name = 'Qəsəbə'
        verbose_name_plural = 'Qəsəbələr'


class Metro(models.Model):
    name = models.CharField(max_length=255, verbose_name='Metro')

    def __str__(self):
        return "{}".format(self.name)
 
    class Meta:
        db_table = 'metros'
        verbose_name = 'Metro'
        verbose_name_plural = 'Metrolar'

    
class Target(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table = 'targets'
        
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(verbose_name='Elektron poçt adresi', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(verbose_name="Şirkət adı", 
                                    max_length=255,null=True,blank=True)
    
    person_in_charge = models.CharField("person_in_charge", max_length=255, )
    phone_number = models.JSONField("Mobil nömrə", max_length=255, unique=True)
    user_type = models.BigIntegerField(verbose_name='Istifadəçi tipi',
                                       choices=USER_TYPE_CHOICES,default=4)
    
    role = models.TextField(verbose_name="role",null=True,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "users"


class Advertisement(models.Model):
    #title = models.CharField(verbose_name='Başlıq', max_length=255, blank=True, null=True, 
    #                         help_text='Qısa başlıq əlavə edin(Qiymət, ünvan, və s)')
    
    room_count = models.BigIntegerField(verbose_name='Otaq sayı', blank=True, null=True)    
    area = models.DecimalField(verbose_name='Sahə',max_digits=10, decimal_places=2, blank=True, 
                               null=True, help_text='Sahə, m² ilə göstərilmişdir')

    area_of_land = models.DecimalField(verbose_name='Torpaq sahəsi', max_digits=10, 
                                       decimal_places=2, blank=True, null=True, 
                                       help_text='Torpaq sahəsi, sot ilə göstərilmişdir')

    coast = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text='Qiymət, manat ilə göstərilmişdir',
                                verbose_name='Qiymət')

    location_width = models.DecimalField(verbose_name='Coğrafi enlik', max_digits=10, 
                                        decimal_places=7, blank=True, null=True, 
                                        help_text='Koordinatı daxil edin')
    
    location_height = models.DecimalField(verbose_name='Coğrafi uzunluq', max_digits=10, 
                                          decimal_places=7, blank=True, null=True, 
                                          help_text='Koordinatı daxil edin')
    
    type = models.BigIntegerField(verbose_name='Tip', choices=ADVERTISEMENT_TYPE_CHOICES)
    sub_type = models.BigIntegerField(choices=ADVERTISEMENT_SUB_TYPE_CHOICES, 
                                      verbose_name='Alt tip',)
    have_government_deed = models.BooleanField(verbose_name='Order', blank=True, null=True, 
                                               default=False,
                                            help_text="Order varsa 'True', yoxdursa 'False' seçin")
    
    have_mortgage_support = models.BooleanField(verbose_name='Ipoteka dəstəyi', blank=True, 
                                                null=True, default=False,
                                                help_text="Ipoteka dəstəyi varsa 'True', yoxdursa 'False' seçin")
    
    building_stage_height = models.BigIntegerField(verbose_name='Bina mərtəbə sayı', 
                                                   blank=True, null=True)
    
    stage = models.BigIntegerField(verbose_name='Mərtəbə', blank=True, null=True)
    description = models.TextField(verbose_name='Ətraflı məlumat', blank=True, null=True)
    view_count = models.BigIntegerField(verbose_name='Baxış sayı')#default=0
    advertisement_create_date = models.DateTimeField(blank=True, null=True)
    advertisement_expire_date = models.DateTimeField(blank=True, null=True)
    advertisement_deleted_date = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='İstifadəçi')
    city_id = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Şəhər',
                                db_constraint=False)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Rayon',
                                  blank=True, null=True, db_constraint=False)
    
    town_ship_id = models.ForeignKey('Township', on_delete=models.CASCADE, 
                                     verbose_name='Qəsəbə', db_constraint=False)    
    metro_id = models.ForeignKey('Metro', on_delete=models.CASCADE, verbose_name='Metro',
                                 blank=True, null=True, db_constraint=False)
    
    target_id = models.ForeignKey('Target', on_delete=models.CASCADE, blank=True, null=True,
                                db_constraint=False)
    repair = models.BooleanField(verbose_name='Təmir', default=False)
    address = models.TextField(verbose_name='Ünvan', blank=True, null=True)
    
    building_type = models.BigIntegerField(verbose_name='Bina Tikili tipi', 
                                           choices=BUILDING_TYPE_CHOICES, null=True, blank=True)
    
    admin_confirmation_status = models.BigIntegerField(choices=ADMIN_CONFIRMATION_STATUS_CHOICES,
                                                        verbose_name='Elan_təsdiqlənmə statusu',
                                                        null=True, blank=True)

    advertisement_type = models.BigIntegerField(choices=ADVERTISEMENT_VIP_TYPE_CHOICES, 
                                                blank=True, null=True, verbose_name='Elan tipi')
    
    advertisement_type_expire_date = models.DateTimeField(null=True, blank=True)
    building_project_type = models.BigIntegerField(choices=BUILDING_PROJECT_TYPE_CHOICES,
                                                   default=3, verbose_name='Mənzil layihə tipi')

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Elan'
        verbose_name_plural = 'Elanlar'
        
        
class Picture(models.Model):
    url = models.CharField(max_length=255)
    advertisement_id = models.ForeignKey('Advertisement', on_delete=models.CASCADE)
    deleted_date = models.DateTimeField(verbose_name='Silinmə tarixi')
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'pictures'
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'  
    
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BigIntegerField(choices=PAYMENT_STATUS_CHOICES)
    order_id = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.email, self.amount)

    class Meta:
        db_table = 'payments'        
        verbose_name = 'Ödəniş'
        verbose_name_plural = 'Ödənişlər'

        
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
        db_table = 'transactions'
        verbose_name = 'Tranzaksiya'
        verbose_name_plural = 'Tranzaksiyalar'
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, Permission, Group,)
from django.utils import timezone

from .managers import CustomUserManager, NormalUserManager

from .constants import (ADVERTISEMENT_TYPE_CHOICES, ADVERTISEMENT_SUB_TYPE_CHOICES,
                        BUILDING_TYPE_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES,
                        ADMIN_CONFIRMATION_STATUS_CHOICES, ADVERTISEMENT_VIP_TYPE_CHOICES,
                        USER_TYPE_CHOICES, BUILDING_PROJECT_TYPE_CHOICES,
                        PAYMENT_STATUS_CHOICES, TRANSACTION_OPERATION_CHOICES)


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Şəhər', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Şəhər'
        verbose_name_plural = 'Şəhərlər'
        db_table = 'cities'



class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name='Rayon', blank=True, null=True)
    city_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'regions'
        verbose_name = 'Rayon'
        verbose_name_plural = 'Rayonlar'


class Township(models.Model):
    name = models.CharField(verbose_name="Qəsəbə", max_length=255, null=True, blank=True)
    region_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'townships'
        verbose_name = 'Qəsəbə'
        verbose_name_plural = 'Qəsəbələr'


class Metro(models.Model):
    name = models.CharField(max_length=255, verbose_name='Metro', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'metros'
        verbose_name = 'Metro'
        verbose_name_plural = 'Metrolar'


class Target(models.Model):
    name = models.CharField(verbose_name='Nişangah', max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'targets'
        verbose_name = 'Nişangah'
        verbose_name_plural = 'Nişangahlar'


class NormalUser(AbstractBaseUser):
    """
    This table refers to normal user

    """

    email = models.EmailField(verbose_name='Elektron poçt adresi', unique=True)
    company_name = models.CharField(verbose_name="Şirkət adı",max_length=255, null=True, blank=True)                                    
    person_in_charge = models.CharField(verbose_name="Əlaqədər şəxs", max_length=255, )
    phone_number = models.JSONField(verbose_name="Mobil nömrə", max_length=13)
    user_type = models.BigIntegerField(verbose_name='Istifadəçi tipi',
                                       choices=USER_TYPE_CHOICES, default=4)

    role = models.TextField(verbose_name="role", null=True, blank=True)

    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['phone_number']

    last_login = None
    objects = NormalUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = 'İstifadəçi'
        verbose_name_plural = 'İstifadəçilər'



class Advertisement(models.Model):
    # title = models.CharField(verbose_name='Başlıq', max_length=255, blank=True, null=True,
    #                         help_text='Qısa başlıq əlavə edin(Qiymət, ünvan, və s)')

    room_count = models.BigIntegerField(verbose_name='Otaq sayı', blank=True, null=True)
    area = models.DecimalField(verbose_name='Sahə', max_digits=10, decimal_places=2, blank=True,
                               null=True, help_text='Sahə, m² ilə göstərilmişdir')

    area_of_land = models.DecimalField(verbose_name='Torpaq sahəsi', max_digits=10,
                                       decimal_places=2, blank=True, null=True,
                                       help_text='Torpaq sahəsi, sot ilə göstərilmişdir')

    coast = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text='Qiymət, manat ilə göstərilmişdir',
                                verbose_name='Qiymət')

    location_width = models.DecimalField(verbose_name='Coğrafi enlik', max_digits=10,
                                         decimal_places=7, blank=True, null=True,
                                         help_text='Koordinatı daxil edin')

    location_height = models.DecimalField(verbose_name='Coğrafi uzunluq', max_digits=10,
                                          decimal_places=7, blank=True, null=True,
                                          help_text='Koordinatı daxil edin')

    type = models.BigIntegerField(verbose_name='Tip', choices=ADVERTISEMENT_TYPE_CHOICES)
    sub_type = models.BigIntegerField(choices=ADVERTISEMENT_SUB_TYPE_CHOICES, 
                                      verbose_name='Alt tip')
    
    have_government_deed = models.BooleanField(verbose_name='Order', blank=True, null=True,
                                               default=False,
                                               help_text="Order varsa 'True', yoxdursa 'False' seçin")

    have_mortgage_support = models.BooleanField(verbose_name='Ipoteka dəstəyi', blank=True,
                                                null=True, default=False,
                                                help_text="Ipoteka dəstəyi varsa 'True', yoxdursa 'False' seçin")

    building_stage_height = models.BigIntegerField(verbose_name='Bina mərtəbə sayı',
                                                   blank=True, null=True)

    stage = models.BigIntegerField(verbose_name='Mərtəbə', blank=True, null=True)
    description = models.TextField(verbose_name='Ətraflı məlumat', blank=True, null=True)
    view_count = models.BigIntegerField(verbose_name='Baxış sayı')  # default=0
    advertisement_create_date = models.DateTimeField(blank=True, null=True)
    advertisement_expire_date = models.DateTimeField(blank=True, null=True)
    advertisement_deleted_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('NormalUser', on_delete=models.DO_NOTHING, verbose_name='İstifadəçi',
                             db_index=True, to_field='email')

    city_id = models.BigIntegerField(verbose_name='Şəhər',)
    
    region_id = models.BigIntegerField(verbose_name='Rayon', blank=True, null=True)

    town_ship_id = models.BigIntegerField(verbose_name='Qəsəbə')
    
    metro_id = models.BigIntegerField(verbose_name='Metro', blank=True, null=True)

    target_id = models.BigIntegerField('Target', blank=True, null=True)
    
    repair = models.BooleanField(verbose_name='Təmir', default=False)
    address = models.TextField(verbose_name='Ünvan', blank=True, null=True)

    building_type = models.BigIntegerField(verbose_name='Bina Tikili tipi',
                                           choices=BUILDING_TYPE_CHOICES)

    admin_confirmation_status = models.BigIntegerField(choices=ADMIN_CONFIRMATION_STATUS_CHOICES,
                                                       verbose_name='Elan_təsdiqlənmə statusu',
                                                       null=True, blank=True)

    advertisement_type = models.BigIntegerField(choices=ADVERTISEMENT_VIP_TYPE_CHOICES,
                                                verbose_name='Elan tipi')

    advertisement_type_expire_date = models.DateTimeField(null=True, blank=True)
    building_project_type = models.BigIntegerField(choices=BUILDING_PROJECT_TYPE_CHOICES,
                                                   verbose_name='Mənzil layihə tipi')

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Elan'
        verbose_name_plural = 'Elanlar'


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.BigIntegerField(choices=PAYMENT_STATUS_CHOICES, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    session = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.user.email, self.amount)

    class Meta:
        db_table = 'payments'
        verbose_name = 'Ödəniş'
        verbose_name_plural = 'Ödənişlər'
        
        
class Transaction(models.Model):
    start_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    end_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    operation = models.PositiveIntegerField(choices=TRANSACTION_OPERATION_CHOICES,  
                                            blank=True, null=True)

    order = models.CharField(max_length=255, blank=True, null=True)
    session = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('NormalUser', on_delete=models.DO_NOTHING, db_index=False,
                             db_constraint=False)

    def __str__(self):
        return '{} - {}'.format(self.operation, self.amount)

    class Meta:
        db_table = 'transactions'
        verbose_name = 'Tranzaksiya'
        verbose_name_plural = 'Tranzaksiyalar'


class Picture(models.Model):
    url = models.CharField(max_length=255)
    advertisement = models.ForeignKey('Advertisement', db_index=False, on_delete=models.DO_NOTHING)
    deleted_date = models.DateTimeField(verbose_name='Silinmə tarixi')

    def __str__(self):
        return "{}".format(self.url)

    class Meta:
        db_table = 'pictures'
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'
        

class CustomUser(AbstractBaseUser, PermissionsMixin):

    """
    This table refers to superusers or admin

    """

    email = models.EmailField(verbose_name='Elektron poçt adresi', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    phone_number = models.JSONField("Mobil nömrə", max_length=13)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "admin_users"


