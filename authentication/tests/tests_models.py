from django.test import TestCase

from authentication.models import Account

from datetime import date

class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(email='john@example.com', date_of_birth=date(1989, 3, 12), password='secret', username='john')
        Account.objects.create(email='admin@example.com', date_of_birth=date(1990, 12, 20), password='secret', username='admin')
    
    def test_user_is_staff(self):
        """
        Tests if the user has is_staff property properly setting.
        """
        admin = Account.objects.get(username='admin')
        john = Account.objects.get(username='john')
        
        admin.is_admin = True
        admin.save()
        
        self.assertFalse(john.is_staff)
        self.assertTrue(admin.is_staff)
    
    def test_full_name(self):
        """
        Tests if Account.full_name method return the correct user full name.
        """
        john = Account.objects.get(username='john')
        john.first_name = 'John'
        john.last_name = 'Doe'
        john.save()
        
        self.assertEqual(john.get_full_name(), 'John Doe')
    
    def test_short_name(self):
        """
        Tests if Account.short_name method return the correct user short name.
        """
        john = Account.objects.get(username='john')
        john.first_name = 'John'
        john.save()
        
        self.assertEqual(john.get_short_name(), 'John')
    
    def test___str__(self):
        """
        Tests if Account.__str__() return the correct user email.
        """
        john = Account.objects.get(username='john')
        
        self.assertEqual(john.__str__(), 'john@example.com')