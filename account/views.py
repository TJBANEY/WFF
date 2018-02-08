import logging

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


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

				user = authenticate(username=email[:30], password=password)
				login(request, user)

				return HttpResponseRedirect('/plants/explore')

			except Exception as e:
				logging.error(e)

	else:
		form = RegisterForm()

	context = {'form': form}

	if request.user.is_active:
		context['logged_in'] = True
	else:
		context['logged_in'] = False

	return render(request, 'account/register.html', context)


def register_plants(request):
	user_complete = True

	if request.method == 'POST':
		return HttpResponseRedirect('register/payment')
	else:
		context = {
			'user_complete': user_complete,
		}

		if request.user.is_active:
			context['logged_in'] = True
		else:
			context['logged_in'] = False

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

	if request.user.is_active:
		context['logged_in'] = True
	else:
		context['logged_in'] = False

	return render(request, 'account/register_payment.html', context)

def sign_in(request):

	if request.method == 'POST':
		form = LoginForm(data=request.POST)

		if form.is_valid():
			login(request, form.get_user())

			return HttpResponseRedirect('/calendar.html')

	else:
		form = LoginForm()

	return render(request, 'account/sign_in.html', {'form': form})

def sign_out(request):
	logout(request)

	return HttpResponseRedirect('/')

@login_required
def my_garden(request):
	try:
		account = Account.objects.get(logon_credentials=request.user)
	except Account.DoesNotExist:
		return HttpResponseRedirect('/account/sign-in')

	context = {
		'account': account,
		'user_plants': account.plants.all(),
	}

	return render(request, "account/my_garden.html", context)
