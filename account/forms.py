import logging

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from account.models import Account


class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput())

	def __init__(self, request=None, *args, **kwargs):
		self.cached_user = None
		self.request = request
		kwargs.setdefault('label_suffix', '')
		super(LoginForm, self).__init__(*args, **kwargs)

	def clean(self):
		cleaned_data = self.cleaned_data

		if len(self._errors) > 0:
			return cleaned_data

		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		generated_username = email[:30]

		if email is None or password is None:
			return forms.ValidationError("Please enter an email and password.")
		else:
			try:
				self.cached_user = authenticate(username=generated_username[:30], password=password)
			except Exception as e:
				logging.error(e)
				self.cached_user = None

		if not self.cached_user:
			self._errors['main'] = self.error_class(["Please enter a correct email and password. Passwords are case sensitive."])
			# self._errors['email'] = self.error_class(["Please enter a correct email and password. Passwords are case sensitive."])

	def get_user(self):
		return self.cached_user


class RegisterForm(forms.ModelForm):
	email = forms.CharField(label="Email", required=True)
	password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput())
	password_verify = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput())

	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'logon_credentials', 'phone', 'address', 'address2', 'city', 'state', 'zip']

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
