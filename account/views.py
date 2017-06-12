from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from account.forms import RegisterForm
from account.models import Account


def register(request):
	x = 5

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			cleaned_data = form.cleaned_data

			if 'email' in request.POST:
				email = request.POST['email']

			if 'password' in request.POST:
				password = request.POST['password']

			account_user = User()
			account_user.email = email
			account_user.password = password
			account_user.save()

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

		else:
			print(form.errors)

	else:
		form = RegisterForm()

	context = {'form': form}

	return render(request, 'account/register.html', context)
