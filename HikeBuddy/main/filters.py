import django_filters

from .models import *

class HostingPlaceFilter(django_filters.FilterSet):
	class Meta:
		model = HostingPlace
		fields = '__all__'
		exclude = ['username']