from django import forms
from django.contrib.auth.admin import UserAdmin

from authentication.models import Account

class AccountCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    date_of_birth = forms.DateField(
        label='Date de naissance',
        widget=forms.SelectDateWidget(
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
    
    date_of_birth = forms.DateField(
        label='Date de naissance',
        widget=forms.SelectDateWidget(
            empty_label=('Année', 'Mois', 'Jour'),
        ),
    )
    
    class Meta:
        model = Account
        fields = ('email', 'username', 'date_of_birth', 'first_name',
            'last_name', 'delivery_adress', 'delivery_adress_complement',
            'delivery_zip_code', 'delivery_town', 'billing_adress',
            'billing_adress_complement','billing_zip_code', 'billing_town',
            'phone_number', 'tagline', 'password', 'is_admin', 'is_active',
        )
        
        def clean_password(self):
            """
            Regardless of what the user provides, return the initial value.
            This is done here, rather than on the field, because the
            field does not have access to the initial value.
            """
            return self.initial['password']


class AccountAdmin(UserAdmin):
    """
    The forms to add and change user instances
    """
    form = AccountChangeForm
    add_form = AccountCreationForm
    
    list_display = ('email', 'username', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Identifiants', {'fields': ('email', 'username')}),
        ('Informations Personelles', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password1', 'password2')
        }),
    )
    
    search_fields = ('email', 'username')
    ordering = ('username',)
    filter_horizontal = ()
    
    print(form.Meta.model.objects.earliest('created_at').is_admin)
