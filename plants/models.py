from django.db import models
from filebrowser.fields import FileBrowseField

# Create your models here.

PLANT_TYPES = (
	('FL', 'Flower'),
	('VG', 'Vegetable'),
	('SH', 'Shrub'),
	('TR', 'Tree'),
)

USE_TYPES = (
	('LA', 'Large Arrangement'),
	('SA', 'Small Arrangement'),
	('BF', 'Body Flower / Corsage'),
	('LO', 'Landscape Only'),
)

LENGTH_UNITS = (
	('IN', 'Inches'),
	('FT', 'Feet'),
	('CM', 'Centimeters'),
	('MT', 'Meters')
)

HARD_ZONES = (
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
	('SD', 'Seed'),
	('PL', 'Plug'),
	('PP', 'Potted Plant'),
)

GERM_CHOICES = (
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

class Plant(models.Model):
	botanical_name = models.CharField(max_length=500, null=True, blank=True)
	plant_type = models.CharField(max_length=255, choices=PLANT_TYPES, default='FL')
	bloom_color = models.CharField(max_length=255, null=True, blank=True)
	best_use = models.CharField(max_length=255, choices=USE_TYPES, default='LA')
	stem_length = models.FloatField(default=1)
	stem_length_units = models.CharField(max_length=255, choices=LENGTH_UNITS, default='IN')
	hardiness_zone = models.CharField(max_length=255, choices=HARD_ZONES, default='1A')
	bloom_time = models.DateField(auto_now_add=True)
	availability = models.CharField(max_length=255, choices=PLANT_AVAILABILITY)
	source = models.ManyToManyField('MaterialSource')
	seed_prep = models.CharField(max_length=255, null=True, blank=True)
	germination = models.CharField(max_length=255, choices=GERM_CHOICES)
	seedling_image = FileBrowseField(max_length=300, null=True, blank=True)
	light_req = models.TextField(max_length=10000, help_text='Light Requirements Following Germination', null=True, blank=True)
	temp_req = models.TextField(max_length=10000, help_text='Temperature Requirements for Germination and Root Development', null=True, blank=True)
	harvest_time_start = models.DateField(auto_now_add=True)
	harvest_time_end = models.DateField(auto_now_add=True)
	cond_methods = models.CharField(max_length=255, help_text='Conditioning Methods', null=True, blank=True)
	tips_and_tricks = models.TextField(max_length=10000, null=True, blank=True)

	def __str__(self):
		return self.botanical_name

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
