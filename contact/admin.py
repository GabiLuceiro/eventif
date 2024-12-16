from django.contrib import admin
from  contact.models import ContactModel
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 
                    'created_at', 'response', 'r_created_at', 'flag']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 
                     'message', 'response']
    list_filter = ['flag', 'created_at']

admin.site.register(ContactModel, AdminContact)
