from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
	model = Account

	list_display = ("first_name", "last_name", "logon_credentials", "address", "city", "state", "zip", "created_on")

admin.site.register(Account, AccountAdmin)
