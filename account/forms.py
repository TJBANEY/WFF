from django import forms
from django.contrib import messages

from account.models import Account


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'logon_credentials', 'phone', 'address', 'address2', 'city', 'state']

	# def clean(self):
	# 	cleaned_data = self.cleaned_data
	#
	# 	password = cleaned_data['password']
	# 	conf_pass = cleaned_data['conf_password']
	#
	# 	if password != conf_pass:
	# 		msg = u'Passwords do not match'
	# 		self._errors['password'] = self.error_class([msg])
	#
	# 	return cleaned_data