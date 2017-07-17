from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from account.models import Account


class RegisterForm(forms.ModelForm):
	email = forms.CharField(label="Email", required=True)
	password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput())
	password_verify = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput())

	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'logon_credentials', 'phone', 'address', 'address2', 'city', 'state']

	def clean(self):
		cleaned_data = self.cleaned_data

		# If there are already errors then no need to go further
		if len(self._errors) > 0:
			return self.cleaned_data

		password = cleaned_data.get('password')
		conf_pass = cleaned_data.get('password_verify')
		email = cleaned_data.get('email')

		# Check Passwords
		if len(password) < 5:
			self._errors["password"] = self.error_class(
				["Passwords must be at least 5 characters long."])
			return self.cleaned_data

		if conf_pass != password:
			self._errors["password"] = self.error_class(
				["Password and confirm password did not match."])
			return self.cleaned_data

		if len(User.objects.filter(username=email[:30])) > 0:
			self._errors["email"] = self.error_class(
				["An account with this email already exist. Please use another one."])
			return self.cleaned_data

		return cleaned_data
