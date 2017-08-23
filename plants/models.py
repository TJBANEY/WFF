import csv

from django.db import models
from django.utils.text import slugify

from account.models import Account
from filebrowser.fields import FileBrowseField
# from selenium import webdriver

# Create your models here.

PLANT_TYPES = (
	('NA', '---'),
	('HB', 'Herb'),
	('SH', 'Shrub'),
	('TR', 'Tree'),
	('GR', 'Grass')
)

USE_TYPES = (
	('NA', '---'),
	('LA', 'Large Arrangement'),
	('SA', 'Small Arrangement'),
	('BF', 'Body Flower / Corsage'),
	('LO', 'Landscape Only'),
)

HARD_ZONES = (
	('NA', '--'),
	('1A', '1A'),
	('1B', '1B'),
	('2A', '2A'),
	('2B', '2B'),
	('3A', '3A'),
	('3B', '3B'),
	('4A', '4A'),
	('4B', '4B'),
	('5A', '5A'),
	('5B', '5B'),
	('6A', '6A'),
	('6B', '6B'),
	('7A', '7A'),
	('7B', '7B'),
	('8A', '8A'),
	('8B', '8B'),
	('9A', '9A'),
	('9B', '9B'),
	('10A', '10A'),
	('10B', '10B'),
	('11A', '11A'),
	('11B', '11B'),
	('12A', '12A'),
	('12B', '12B'),
	('13A', '13A'),
	('13B', '13B'),
)

PLANT_AVAILABILITY = (
	('NA', '----'),
	('SD', 'Seed'),
	('PL', 'Plug'),
	('PP', 'Potted Plant'),
)

GERM_CHOICES = (
	('NA', '-----'),
	('NL', 'Needs Light'),
	('ND', 'Needs Darkness'),
	('NA', 'Neither')
)

PLANT_DEPTH = (
	('CV', 'Cover'),
	('BR', 'Bury'),
	('LC', 'Lightly Cover'),
	('SS', 'Surface Sow')
)

COND_METHODS = (
	('QD', 'Quick Dip'),
	('HS', 'Heat Seal'),
	('FF', 'Flower Food'),
	('WW', 'Warm Water'),
	('CW', 'Cold Water'),
	('HD', 'Hold Dry In Cooler'),
)

EVENT_TYPES = (
	('PT', 'Plant Seeds'),
	('MV', 'Move Plants'),
	('PR', 'Prune Plants'),
	('HV', 'Harvest'),
	('OT', 'Other'),
)

class Plant(models.Model):
	usda_code = models.CharField(max_length=100, null=True, blank=True)
	scientific_name = models.CharField(max_length=500, null=True, blank=True)
	botanical_name = models.CharField(max_length=500, null=True, blank=True)
	perennial = models.BooleanField(default=False)
	biennial = models.BooleanField(default=False)
	annual = models.BooleanField(default=False)
	growth_habit = models.CharField(max_length=255, default='NA')
	foliage_color = models.CharField(max_length=255, null=True, blank=True)
	flower_color = models.CharField(max_length=255, null=True, blank=True)
	best_use = models.CharField(max_length=255, choices=USE_TYPES, default='NA')
	stem_length = models.FloatField(default=1, help_text='Always in centimeters')
	hardiness_zone = models.CharField(max_length=255, choices=HARD_ZONES, default='NA')
	bloom_time = models.DateField(null=True, blank=True)
	availability = models.CharField(max_length=255, choices=PLANT_AVAILABILITY, default='NA')
	source = models.ManyToManyField('MaterialSource', blank=True)
	seed_prep = models.CharField(max_length=255, null=True, blank=True)
	germination = models.CharField(max_length=255, choices=GERM_CHOICES, default='NA')
	seedling_image = FileBrowseField(max_length=300, null=True, blank=True)
	light_req = models.TextField(max_length=10000, help_text='Light Requirements Following Germination', null=True,
								 blank=True)
	temp_req = models.TextField(max_length=10000,
								help_text='Temperature Requirements for Germination and Root Development', null=True,
								blank=True)
	harvest_time_start = models.DateField(null=True, blank=True)
	harvest_time_end = models.DateField(null=True, blank=True)
	cond_methods = models.CharField(max_length=255, help_text='Conditioning Methods', null=True, blank=True)
	tips_and_tricks = models.TextField(max_length=10000, null=True, blank=True)

	slug = models.SlugField(null=True, blank=True)

	is_published = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.botanical_name)

		super(Plant, self).save(*args, **kwargs)

	def __str__(self):
		return 'Plant'

	class Meta:
		verbose_name = "Plant"
		verbose_name_plural = "Plants"
		ordering = ("scientific_name",)


class PlantImage(models.Model):
	plant = models.ForeignKey(Plant, related_name="images")
	image = models.ImageField(upload_to="images", max_length=300, null=True, blank=True)
	image_url = models.URLField(null=True, blank=True)

	def __str__(self):
		return 'Image for {}'.format(self.plant.botanical_name)


class PlantEvent(models.Model):
	event_type = models.CharField(max_length=255, choices=EVENT_TYPES, null=True, blank=True)
	name = models.CharField(max_length=255, help_text='e.g. Plant seeds, Move to larger pot, etc.', null=True,
							blank=True)
	plant = models.ForeignKey(Plant, related_name='events', null=True, blank=True)
	event_start = models.DateTimeField(null=True, blank=True)
	event_end = models.DateTimeField(null=True, blank=True)
	details = models.TextField(max_length=10000, null=True, blank=True)
	color = models.CharField(default='1bc974', max_length=10, null=True, blank=True,
							 help_text='This will be the color of the event on the dashboard calendar')
	text_color = models.CharField(default='fff', max_length=6, null=True, blank=True,
								  help_text='This will be the color the event text on the dashboard calendar')

	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class Region(models.Model):
	continent = models.CharField(max_length=255)
	country = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)


class MaterialSource(models.Model):
	name = models.CharField(max_length=255)
	site = models.URLField()
	address = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True)


class SpecialRequirement(models.Model):
	plant = models.ForeignKey(Plant)
	requirement = models.CharField(max_length=500)

	def __str__(self):
		return 'Requirement for {}'.format(self.plant.botanical_name)


class PestIssue(models.Model):
	plant = models.ForeignKey(Plant)
	pest = models.CharField(max_length=255)
	details = models.TextField(max_length=10000, null=True, blank=True)

	def __str__(self):
		return self.pest


class UserPlant(models.Model):
	user = models.ForeignKey(Account)
	plant = models.ForeignKey(Plant)

	def __str__(self):
		return '{} {} - {}'.format(self.user.first_name, self.user.last_name, self.plant.botanical_name)

	class Meta:
		unique_together = ("user", "plant")


def dump(qs, outfile_path):
	"""
	Takes in a Django queryset and spits out a CSV file.

	Usage::

		>> from utils import dump2csv
		>> from dummy_app.models import *
		>> qs = DummyModel.objects.all()
		>> dump2csv.dump(qs, './data/dump.csv')

	Based on a snippet by zbyte64::

		http://www.djangosnippets.org/snippets/790/

	"""
	model = qs.model
	writer = csv.writer(open(outfile_path, 'w'))

	headers = []
	for field in model._meta.fields:
		headers.append(field.name)
	writer.writerow(headers)

	for obj in qs:
		row = []
		for field in headers:
			val = getattr(obj, field)
			if callable(val):
				val = val()
			# if type(val) == unicode:
			# 	val = val.encode("utf-8")
			row.append(val)
		writer.writerow(row)
