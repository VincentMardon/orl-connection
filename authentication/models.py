from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from authentication.services import calculate_age


# -------------- #
# AccountManager #
# -------------- #

class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of birth,
        password and username.
        """
        
        if not email:
            raise ValueError('L\'utilisateur doit avoir un email valide.')
        
        if not kwargs.get('username'):
            raise ValueError('L\'utilisateur doit avoir un nom d\'utilisateur.')
        
        if calculate_age(date_of_birth) < 13:
            raise ValueError('L\'utilisateur doit avoir 13 ans minimum.')
        
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


# ------- #
# Account #
# ------- #

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True, verbose_name='Nom d\'utilisateur')
    date_of_birth = models.DateField(verbose_name='Date de naissance')
    
    first_name = models.CharField(null=True, max_length=40, verbose_name='Prénom')
    last_name = models.CharField(null=True, max_length=40, verbose_name='Nom de famille')
    
    delivery_adress = models.CharField(null=True, max_length=255, verbose_name='Adresse')
    delivery_adress_complement = models.CharField(null=True, max_length=255, verbose_name='Complément d\'adresse')
    delivery_zip_code = models.IntegerField(null=True, verbose_name='Code postal')
    delivery_town = models.CharField(null=True, max_length=50, verbose_name='Ville')
    
    billing_adress = models.CharField(null=True, max_length=255, verbose_name='Adresse')
    billing_adress_complement = models.CharField(null=True, max_length=255, verbose_name='Complément d\'adresse')
    billing_zip_code = models.IntegerField(null=True, verbose_name='Code postal')
    billing_town = models.CharField(null=True, max_length=50, verbose_name='Ville')
    
    phone_number = models.IntegerField(null=True, verbose_name='Numéro de téléphone')
    tagline = models.CharField(null=True, max_length=140, verbose_name='Signature')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Mise à jour')
    
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    is_admin = models.BooleanField(default=False, verbose_name='Administrateur')
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']
    
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
    
    @property
    def is_staff(self):
        return self.is_admin
