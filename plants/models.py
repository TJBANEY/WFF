from django.db import models

# Create your models here.

class Plant(models.Model):
	name = models.CharField(max_length=255)
	genus = models.CharField(max_length=255)
	species = models.CharField(max_length=255)
	family = models.CharField(max_length=255)
	type = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	native_region = models.ManyToManyField(Region)


class Region(models.Model):
	continent = models.CharField(max_length=255)
	country = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)