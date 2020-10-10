from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, full_name, phone, address, avatar, gender, date_join, date_of_birth, is_superuser=False, is_reporter=False, is_staff=False, is_active=True, password=None):
        if not username:
            raise ValueError('You must have a Username')
        if not password:
            raise ValueError('You must Create A password')
        user = self.model(
            username=username,
            email=email,
            full_name=full_name,
            address=address,
            phone=phone,
            avatar=avatar,
            gender=gender,
            date_join=datetime.date.today(),
            date_of_birth=date_of_birth,
            is_superuser=is_superuser,
            is_reporter=is_reporter,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            email='',
            full_name='',
            address='',
            phone=0,
            avatar='',
            gender=True,
            date_join=datetime.date.today(),
            date_of_birth=datetime.date.today(),
            is_superuser=True,
            is_reporter=True,
            is_staff=True,
            is_active=True,
            password=password
        )
        return user


    def create_staff_user(self, username, email, full_name, phone, address, avatar, gender, date_of_birth, password=None):
        user = self.create_user(
            username=username,
            email=email,
            full_name=full_name,
            address=address,
            phone=phone,
            avatar=avatar,
            gender=gender,
            date_join=datetime.date.today(),
            date_of_birth=date_of_birth,
            is_superuser=False,
            is_reporter=True,
            is_staff=True,
            is_active=True,
        )
        return user


    def create_reporter(self, username, email, full_name, phone, address, avatar, gender, date_of_birth, password=None):
        user = self.create_user(
            username=username,
            email=email,
            full_name=full_name,
            address=address,
            phone=phone,
            avatar=avatar,
            gender=gender,
            date_join=datetime.date.today(),
            date_of_birth=date_of_birth,
            is_superuser=False,
            is_reporter=True,
            is_staff=False,
            is_active=True,
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=254, default='')
    full_name = models.CharField(max_length=75, default='')
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=95, default='')
    avatar = models.ImageField(upload_to='static/img/avatar/', default='static/img/avatar/default.jpg')
    gender = models.BooleanField(default=True)
    date_join = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(default='2000-01-01')
    is_superuser = models.BooleanField(default=False)
    is_reporter = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELD = [''] # when run python manage.py createsuperuser

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_user(self):
        return self.username

    def staff_check(self):
        if self.is_staff == True:
            return True
        else:
            return False

    def super_check(self):
        if self.is_superuser == True:
            return True
        else:
            return False

    def reporter_check(self):
        if self.is_reporter == True:
            return True
        else:
            return False

    def active_check(self):
        if self.is_staff == True:
            return True
        else:
            return False
    
    def gender_field(self):
        if self.gender == True:
            return 'Male'
        else:
            return 'Female'
    
    def get_full_name(self):
        return self.full_name