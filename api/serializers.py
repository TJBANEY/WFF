from account.models import Account
from rest_framework import serializers
from plants.models import Plant, PlantEvent, UserPlant


class UserPlantSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'user',
			'plant'
		)
		model = UserPlant

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'first_name',
			'last_name',
			'phone',
			'address',
			'address2',
			'city',
			'state'
		)
		model = Account

class PlantEventSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'event_type',
			'name',
			'plant',
			'event_start',
			'event_end',
			'details',
			'color'
		)
		model = PlantEvent

class PlantSerializer(serializers.ModelSerializer):
	events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		fields = (
			'id',
			'scientific_name',
			'botanical_name',
			'growth_habit',
			'flower_color',
			'foliage_color'
			'best_use',
			'stem_length',
			'hardiness_zone',
			'availability',
			'source',
			'seed_prep',
			'germination',
			'seedling_image',
			'light_req',
			'temp_req',
			'harvest_time_start',
			'harvest_time_end',
			'cond_methods',
			'tips_and_tricks',
			'events',
		)
		model = Plant
