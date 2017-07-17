import logging

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from account.forms import RegisterForm, LoginForm
from account.models import Account
from plants.models import Plant


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			cleaned_data = form.cleaned_data

			if 'email' in request.POST:
				email = request.POST['email']

			if 'password' in request.POST:
				password = request.POST['password']

			try:
				account_user = User.objects.create_user(email[:30], email, password, first_name=cleaned_data['first_name'],
														last_name=cleaned_data['last_name'])

				account = Account()
				account.first_name = cleaned_data['first_name']
				account.last_name = cleaned_data['last_name']
				account.logon_credentials = account_user
				account.phone = cleaned_data['phone']
				account.address = cleaned_data['address']
				account.address2 = cleaned_data['address2']
				account.city = cleaned_data['city']
				account.state = cleaned_data['state']

				account.save()

				login(request, account_user)

				return HttpResponseRedirect('register/plants')

			except Exception as e:
				logging.error(e)

	else:
		form = RegisterForm()

	context = {'form': form}

	return render(request, 'account/register.html', context)


def register_plants(request):
	user_complete = True

	if request.method == 'POST':
		return HttpResponseRedirect('register/payment')
	else:
		context = {
			'user_complete': user_complete,
		}

		return render(request, 'account/register_plants.html', context)

def register_payment(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/calendar')

	plants_complete = True
	user_complete = True

	context = {
		'user_complete': user_complete,
		'plants_complete': plants_complete
	}

	return render(request, 'account/register_payment.html', context)

def sign_in(request):

	if request.method == 'POST':
		form = LoginForm(data=request.POST)

		if form.is_valid():
			login(request, form.get_user())

			return HttpResponseRedirect('/calendar')

	else:
		form = LoginForm()

	return render(request, 'account/sign_in.html', {'form': form})

