from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from datetime import date

class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of birth,
        password and username.
        """
        
        if not email:
            raise ValueError('User must have an email adress.')
        
        if not kwargs.get('username'):
            raise ValueError('User must have a username.')
        
        if calculate_age(date_of_birth) < 13:
            raise ValueError('User must be 13 at least.')
        
        account = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=kwargs.get('username')
        )
        
        account.set_password(password)
        account.save()
        
        return account
    
    def create_superuser(self, email, date_of_birth, password, **kwargs):
        """
        Creates and saves a superuser with the given email, date_of_birth,
        password and username.
        """
        account = self.create_user(email, date_of_birth, password, **kwargs)
        
        account.is_admin = True
        account.save()
        
        return account
    
    def calculate_age(born):
        """
        Calculates the user age
        """
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    date_of_birth = models.DateField()
    
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adress = models.CharField(max_length=255)
    adress_complement = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    town = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    tagline = models.CharField(max_length=140)
    
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']
    
    def get_full_name(self):
        """
        Returns user first_name and last_name. 
        """
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def get_short_name(self):
        """
        Returns user first_name.
        """
        return self.first_name
    
    def __str__(self):
        """
        Returns user email
        """
        return self.email