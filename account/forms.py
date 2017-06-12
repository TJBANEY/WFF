from django import forms

from account.models import Account


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'logon_credentials', 'phone', 'address', 'address2', 'city', 'state']

