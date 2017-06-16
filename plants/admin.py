from django.contrib import admin

# Register your models here.
from plants.models import Plant, MaterialSource


class PlantAdmin(admin.ModelAdmin):
	model = Plant

class SourceAdmin(admin.ModelAdmin):
	model = MaterialSource

admin.site.register(Plant, PlantAdmin)
admin.site.register(MaterialSource, SourceAdmin)
