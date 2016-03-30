from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin

from datetime import date

from authentication.models import Account

class AccountCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    # No discrimination, people can create an account until 120 years old !
    available_year = date.today().year - 12
    earliest_year = date.today().year - 120
    
    years = sorted([year for year in range(earliest_year, available_year)], reverse=True)
    
    date_of_birth = forms.DateField(
        label='Date de naissance',
        widget=forms.SelectDateWidget(
            years=years,
            empty_label=('Année', 'Mois', 'Jour'),
        ),
    )
    
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput
    )
    
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'date_of_birth'
        )
    
    def clean_password2(self):
        """
        Check that the two password entries match
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        
        return password2
    
    def save(self, commit=True):
        """
        Save the provided password in hashed format
        """
        user = super(AccountCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user


class AccountChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user,
    but not the password.
    """
    
    class Meta:
        model = Account
        fields = ('email', 'username', 'date_of_birth', 'first_name',
            'last_name', 'delivery_adress', 'delivery_adress_complement',
            'delivery_zip_code', 'delivery_town', 'billing_adress',
            'billing_adress_complement','billing_zip_code', 'billing_town',
            'phone_number', 'tagline', 'password', 'is_admin', 'is_active',
        )


class AccountAdmin(UserAdmin):
    """
    The forms to add and change user instances
    """
    form = AccountChangeForm
    add_form = AccountCreationForm
    
    list_display = ('email', 'username', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password1', 'password2')
        }),
    )
    fieldsets = (
        ('Permissions', {
            'description': 'Cochez/décochez "<b>Administrateur</b>" pour autoriser/interdire l\'utilisateur à accéder à l\'administration.<br />Cochez/décochez "<b>Actif</b>" pour activer/désactiver le compte de l\'utilisateur.',
            'fields': ('is_admin', 'is_active')
        }),
        ('Identifiants', {'fields': ('email', 'username')}),
        ('Informations Personelles', {'fields': (
            'first_name',
            'last_name', 
            'date_of_birth',
            'phone_number',
            'tagline',
        )}),
        ('Adresse de livraison', {'fields': (
            'delivery_adress',
            'delivery_adress_complement',
            'delivery_zip_code',
            'delivery_town',
        )}),
        ('Adresse de facturation', {'fields': (
            'billing_adress',
            'billing_adress_complement',
            'billing_zip_code',
            'billing_town',
        )}),
    )
    
    search_fields = ('email', 'username')
    ordering = ('username',)
    filter_horizontal = ()
    
    def get_readonly_fields(self, request, obj=None):
        """
        Display fields, except is_active and is_admin fields, in readonly_fields
        if obj = form
        """
        readonly_fields = ()
        
        if obj is not None:
            readonly_fields = (
                'email',
                'username',
                'first_name',
                'last_name',
                'date_of_birth',
                'phone_number',
                'tagline',
                'delivery_adress',
                'delivery_adress_complement',
                'delivery_zip_code',
                'delivery_town',
                'billing_adress',
                'billing_adress_complement',
                'billing_zip_code',
                'billing_town',
            )
            
            return readonly_fields
        
        return readonly_fields