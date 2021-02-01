from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, employeId, full_name,Department, password=None):
        if not employeId:
            raise ValueError("Users must have an employeId")
        if not full_name:
            raise ValueError("User must have a name")
        if not Department:
            raise ValueError("Add Department")
        user = self.model(
            employeId=employeId,
            full_name=full_name,
            Department=Department
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, employeId, full_name,Department, password):
        user = self.create_user(
            employeId=employeId,
            password=password,
            full_name=full_name,
            Department=Department
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    employeId = models.CharField(unique=True,max_length=30)
    full_name = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'employeId'
    REQUIRED_FIELDS = [ 'full_name', 'Department',]

    objects = MyAccountManager()

    def __str__(self):
        return "("+str(self.employeId)+")"+str(self.full_name)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    