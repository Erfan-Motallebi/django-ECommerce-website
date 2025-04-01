from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account

class AccountAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_staff', 'is_active']
    list_display_links = ['first_name', 'last_name', 'username']
    readonly_fields = ['last_login', 'date_joined']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)