from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite

from authentication.models import Account
from authentication.admin import AccountAdmin

class ORLAdminSite(AdminSite):
    site_header = "Administration d'orl-connection.com"

admin_site = ORLAdminSite(name='orladmin')

# Registering the new AccountAdmin
admin_site.register(Account, AccountAdmin)

# Since we're not using Django's built-in permissions,
# unregister the Group model from admin
admin.site.unregister(Group)