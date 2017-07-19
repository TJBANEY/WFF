from django.contrib import admin

# Register your models here.
from plants.models import Plant, MaterialSource, PlantEvent, Region, UserPlant


class PlantAdmin(admin.ModelAdmin):
	model = Plant

	list_display = ('botanical_name', 'plant_type', 'bloom_color')

class SourceAdmin(admin.ModelAdmin):
	model = MaterialSource

class PlantEventAdmin(admin.ModelAdmin):
	model = PlantEvent

class RegionAdmin(admin.ModelAdmin):
	model = Region

class UserPlantAdmin(admin.ModelAdmin):
	model = UserPlant

admin.site.register(Plant, PlantAdmin)
admin.site.register(MaterialSource, SourceAdmin)
admin.site.register(PlantEvent, PlantEventAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(UserPlant, UserPlantAdmin)
