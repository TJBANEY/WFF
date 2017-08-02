from django.shortcuts import render

def explore_plants(request):

	context = {}

	return render(request, 'plants/explore.html', context)