from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	logon_credentials = models.ForeignKey(User, null=True, blank=True)
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255, null=True, blank=True)
	address2 = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True)
	zip = models.IntegerField(null=True, blank=True)

	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def get_all_tasks(self):
		from plants.models import PlantTask
		user_plants = self.plants.all()

		tasks = PlantTask.objects.filter(user_plant__in=user_plants).order_by('create_date')
		return tasks

	@staticmethod
	def current_user(request):
		if request.user.is_authenticated:
			try:
				current_user = Account.objects.get(logon_credentials=request.user)
				return current_user
			except Account.DoesNotExist:
				return None
		else:
			return None


	class Meta:
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'
		ordering = ('created_on', 'last_name')