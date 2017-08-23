from django.contrib import admin

# Register your models here.
from plants.models import Plant, MaterialSource, PlantEvent, Region, UserPlant, PlantImage


class PlantAdmin(admin.ModelAdmin):
	model = Plant

	search_fields = ('botanical_name', 'scientific_name')
	list_display = ('id', 'usda_code', 'is_published', 'slug', 'scientific_name', 'botanical_name', 'growth_habit', 'perennial',
					'annual', 'biennial', 'foliage_color', 'flower_color', 'best_use', 'stem_length', 'hardiness_zone',
					'bloom_time', 'availability', 'seed_prep')

class SourceAdmin(admin.ModelAdmin):
	model = MaterialSource

class PlantEventAdmin(admin.ModelAdmin):
	model = PlantEvent

class RegionAdmin(admin.ModelAdmin):
	model = Region

class UserPlantAdmin(admin.ModelAdmin):
	model = UserPlant

class PlantImageAdmin(admin.ModelAdmin):
	model = PlantImage

admin.site.register(Plant, PlantAdmin)
admin.site.register(MaterialSource, SourceAdmin)
admin.site.register(PlantEvent, PlantEventAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(UserPlant, UserPlantAdmin)
admin.site.register(PlantImage, PlantImageAdmin)