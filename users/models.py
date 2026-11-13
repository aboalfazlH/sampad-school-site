from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator as username_validator
from django.core.validators import RegexValidator

REGEXS = {
    "phone_number":r'^(?:(?:\+?98)|0)?9\d{2}[-\s]?\d{3}[-\s]?\d{4}$',
    "natinoal_code":r'^[0-9]{10}$'
}

class User(AbstractUser):
    phone_number = models.CharField(verbose_name="شماره تلفن",validators=[RegexValidator(REGEXS["phone_number"])],max_length=110)
    national_code = models.CharField(verbose_name="کد ملی",max_length=11,validators=[RegexValidator(REGEXS["natinoal_code"])],unique=True)
    display_name = models.CharField(max_length=110,verbose_name="نام نمایشی")
    birth_date = models.DateField(verbose_name="تاریخ تولد",blank=True,null=True)
    username = models.CharField(
            verbose_name="نام کاربری",
            max_length=150,
            unique=True,
            validators=[username_validator],
            error_messages={
                "unique": "یک کاربر با همین نام کاربری وجود دارد",
            },
            blank=True,
            null=True
        )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "national_code"
    REQUIRED_FIELDS = ["email","phone_number","username"]

    def __str__(self):
        if self.display_name:
            name = self.display_name
        
        elif self.get_full_name():
            name = self.get_full_name()
        
        elif self.username:
            name = self.username
        
        else:
            name = self.national_code
        
        return name

class Student(models.Model):
    """دانش آموز"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزش ها'

class Teacher(models.Model):
    """معلم"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'معلم ها'

class Parents(models.Model):
    """والدین"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'ولی'
        verbose_name_plural = 'والدین'

class Deputy(models.Model):
    """معاون"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'معاون'
        verbose_name_plural = 'معاون ها'

class Manager(models.Model):
    """مدیر"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'مدیر'
        verbose_name_plural = 'مدیر ها'

class Consultant(models.Model):
    """مشاور"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'مشاور'
        verbose_name_plural = 'مشاور ها'