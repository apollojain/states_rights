from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Country(models.Model):

	CO = "CO"
	ST = "ST"
	PR = "PR"
	COUNTRY_TYPES = (
		(CO, 'Country'),
		(ST, 'State'), 
		(PR, 'Proposed'),
	)

	name = models.CharField(max_length=200)
	country_type = models.CharField(
		max_length=2, 
		choices=COUNTRY_TYPES, 
		default=PR,
	)

	capital_city = models.CharField(max_length=100, null=True, blank=True)

	description = models.CharField(max_length=2000, null=True, blank=True)

	component_states = models.CharField(max_length=1000, null=True, blank=True)

	total_area = models.IntegerField()
	total_area_rank = models.IntegerField(null=True, blank=True)
	total_area_closest = models.CharField(max_length=100, null=True, blank=True)

	total_population = models.IntegerField()
	total_population_rank = models.IntegerField(null=True, blank=True)
	total_population_closest = models.CharField(max_length=100, null=True, blank=True)

	population_density = models.DecimalField(max_digits = 10, decimal_places = 2)
	population_density_rank = models.IntegerField(null=True, blank=True)
	population_density_closest = models.CharField(max_length=100, null=True, blank=True)

	gdp_total = models.IntegerField()
	gdp_total_rank = models.IntegerField(null=True, blank=True)
	gdp_total_closest = models.CharField(max_length=100, null=True, blank=True)

	gdp_per_capita = models.DecimalField(max_digits = 10, decimal_places = 2)
	gdp_per_capita_rank = models.IntegerField(null=True, blank=True)
	gdp_per_capita_closest = models.CharField(max_length=100, null=True, blank=True)

	gini = models.DecimalField(max_digits = 10, decimal_places = 2)
	gini_rank = models.IntegerField(null=True, blank=True)
	gini_closest = models.CharField(max_length=100, null=True, blank=True)

	life_expectancy = models.DecimalField(max_digits = 10, decimal_places = 2)
	life_expectancy_rank = models.IntegerField(null=True, blank=True)
	life_expectancy_closest = models.CharField(max_length=100, null=True, blank=True)