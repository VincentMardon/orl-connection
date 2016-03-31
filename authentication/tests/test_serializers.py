from django.test import TestCase

from rest_framework.serializers import ValidationError

from authentication.models import Account
from authentication.serializers import AccountSerializer

from datetime import date

class AccountSerializerTestCase(TestCase):
    def setUp(self):
        john = Account.objects.create(email='john@example.com', date_of_birth=date(1989, 3, 12), password='secret', username='john')
        baby = Account.objects.create(email='baby@example.com', date_of_birth=date.today(), password='secret', username='baby')
        
        self.john = AccountSerializer(john)
        self.baby = AccountSerializer(baby)
    
    def test_validate_date_of_birth_success(self):
        """
        Tests if AccountSerializer.validate_date_of_birth method return 
        user.data['date_of_birth'] if the user is of legal age.
        """
        self.assertEqual(self.john.validate_date_of_birth(self.john.data['date_of_birth']), '1989-03-12')
    
    def test_validate_date_of_birth_error(self):
        """
        Tests if AccountSerializer.validate_date_of_birth method raise a 
        ValidationError if the user is too young.
        """
        self.assertRaises(ValidationError, self.baby.validate_date_of_birth, self.baby.data['date_of_birth'])