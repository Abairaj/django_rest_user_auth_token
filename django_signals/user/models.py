from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.


class User_manager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff' ,True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have Staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True') 
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active = True')
        return self.create_user(email,password,**extra_fields)
    


class users(AbstractUser):
        
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(('Email address'),unique=True)
        mobile = models.BigIntegerField()
        password = models.CharField(max_length=100)
        date_joined = models.DateField(auto_now_add=True,null=True,blank=True)

        object = User_manager()
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name','last_name','mobile']


        def __str__(self):
             return self.email
     


