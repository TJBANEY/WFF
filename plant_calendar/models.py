from django.db import models

# Create your models here.

class calendarEvent(models.Model):
	title = models.CharField(max_length=255)
	all_day = models.BooleanField(default=False)
	start = models.DateTimeField(auto_now_add=True)
	end = models.DateTimeField(auto_now_add=True)
	url = models.URLField(null=True, blank=True)
	class_name = models.CharField(max_length=50, null=True, blank=True)
	background = models.CharField(max_length=255, null=True, blank=True)
	border = models.CharField(max_length=255, null=True, blank=True)
	text = models.CharField(max_length=255, null=True, blank=True)