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
        
        if self.calculate_age(date_of_birth) < 13:
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
    
    def calculate_age(self, born):
        """
        Calculates the user age
        """
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True, verbose_name='Nom d\'utilisateur')
    date_of_birth = models.DateField(verbose_name='Date de naissance')
    
    first_name = models.CharField(max_length=40, verbose_name='Prénom')
    last_name = models.CharField(max_length=40, verbose_name='Nom de famille')
    
    delivery_adress = models.CharField(max_length=255, verbose_name='Adresse de livraison')
    delivery_adress_complement = models.CharField(max_length=255, verbose_name='Complément d\'adresse de livraison')
    delivery_zip_code = models.IntegerField(null=True, verbose_name='Code postal de livraison')
    delivery_town = models.CharField(max_length=50, verbose_name='Ville de livraison')
    
    billing_adress = models.CharField(max_length=255, verbose_name='Adresse de facturation')
    billing_adress_complement = models.CharField(max_length=255, verbose_name='Complément d\'adresse de facturation')
    billing_zip_code = models.IntegerField(null=True, verbose_name='Code postal de facturation')
    billing_town = models.CharField(max_length=50, verbose_name='Ville de livraison')
    
    phone_number = models.IntegerField(null=True, verbose_name='Numéro de téléphone')
    tagline = models.CharField(max_length=140, verbose_name='Signature')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Mise à jour')
    
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    is_admin = models.BooleanField(default=False, verbose_name='Administrateur')
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']
    
    class Meta:
        verbose_name = 'Compte utilisateur'
        verbose_name_plural = 'Comptes utilisateur'
    
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
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return self.is_admin
