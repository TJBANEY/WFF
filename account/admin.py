from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
	model = Account

admin.site.register(Account, AccountAdmin)
