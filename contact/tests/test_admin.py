from django.test import TestCase
from contact.admin import AdminContact

class Admin(TestCase):
    def test_listDisplay(self):
        self.assertEqual(AdminContact.list_display, [
            'name', 
            'email', 
            'phone', 
            'message', 
            'created_at', 
            'response', 
            'r_created_at', 
            'flag'
            ])