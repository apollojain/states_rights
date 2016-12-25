from cumulation.models import Country
import pandas as pd 
import numpy as np 
import sys

states_file = "cumulation/static/spreadsheets/states_data.xls"
countries_file = "cumulation/static/spreadsheets/nations_information.xls"

def format_country(country):
	if country[0] == ' ' or country[0].isalpha() is False:
		return country[1:]
	country = ''.join([x for x in country if (x.isalpha() or x.isspace())])
	country = country.split(' ')
	country = ' '.join([word.lower().capitalize() for word in country if word != ''])
	
	return country

def create_country(cleaned_data):
	name = str(cleaned_data['country_name'])
	selected_states = str(cleaned_data['selected_states'])
	states_array = selected_states.split(', ')
	capital_city = str(cleaned_data['capital_city'])
	description = str(cleaned_data['description'])
	dictionary = process_states(states_array)

	c = Country()
	c.name = name
	c.capital_city = capital_city
	c.description = description

	c.component_states = selected_states

	c.total_area = dictionary["Area"]
	c.total_area_rank = dictionary["Area Rank"]
	c.total_area_closest = dictionary["Area Closest"]

	c.total_population = dictionary["Population"]
	c.total_population_rank = dictionary["Population Rank"]
	c.total_population_closest = dictionary["Population Closest"]

	c.population_density = dictionary["Population Density"]
	c.population_density_rank = dictionary["Population Density Rank"]
	c.population_density_closest = dictionary["Population Density Closest"]

	c.gdp_total = dictionary["Gross Domestic Product"]
	c.gdp_total_rank = dictionary["Gross Domestic Product Rank"]
	c.gdp_total_closest = dictionary["Gross Domestic Product Closest"]

	c.gdp_per_capita = dictionary["GDP Per Capita"]
	c.gdp_per_capita_rank = dictionary["GDP Per Capita Rank"]
	c.gdp_per_capita_closest = dictionary["GDP Per Capita Closest"]

	c.gini = dictionary["Gini Coefficient"]
	c.gini_rank = dictionary["Gini Coefficient Rank"]
	c.gini_closest = dictionary["Gini Coefficient Closest"]

	c.life_expectancy = dictionary["Life Expectancy"]
	c.life_expectancy_rank = dictionary["Life Expectancy Rank"]
	c.life_expectancy_closest = dictionary["Life Expectancy Closest"]

	c.save()
	return c

def read_excel(filename):
	df = pd.read_excel(filename)
	all_states = {}
	rows = df.shape[0]
	for i in range(rows):
		dictionary = {}
		data = df.iloc[i]		
		dictionary["Name"] = data["Name"]
		dictionary["Area"] = data["Area"]
		dictionary["Population"] = data["Population"]
		dictionary["Gross Domestic Product"] = data["Gross Domestic Product"]
		dictionary["GDP Per Capita"] = data["GDP Per Capita"]
		dictionary["Gini Coefficient"] = data["Gini Coefficient"]
		dictionary["Life Expectancy"] = data["Life Expectancy"]
		
		abbreviation = data["Abbreviation"]
		all_states[abbreviation] = dictionary

	return all_states



def match_state(value, sheetname):
	df = pd.read_excel(countries_file, sheetname = sheetname)
	rows = df.shape[0]
	diff = lambda x: abs(float(value) - float(x))
	best_key = None
	best_value = float(sys.maxint)
	best_ranking = None
	for i in range(rows):
		data = df.iloc[i]
		country = data["Country"]
		cur_val = data["Value"]
		ranking = data["Rank"]
		if diff(cur_val) < diff(best_value): 

			best_key = format_country(country)
			best_value = cur_val
			best_ranking = ranking
			print best_key, best_value, best_ranking
	return (best_ranking, best_key)

def assign_ranks_and_similar(dictionary):
	keys = dictionary.keys()
	for k in keys: 
		print "------KEY-------"
		print k
		r = k + " Rank"
		c = k + " Closest"
		dictionary[r], dictionary[c] = match_state(dictionary[k], k)
		dictionary[r] = int(dictionary[r])
	return dictionary

def process_states(states_array):
	all_states = read_excel(states_file)
	
	dictionary = {}
	dictionary["Area"] = 0
	dictionary["Population"] = 0
	dictionary["Gross Domestic Product"] = 0
	dictionary["Gini Coefficient"] = 0
	dictionary["Life Expectancy"] = 0
	for state in states_array: 
		dictionary["Area"] += all_states[state]["Area"]
		dictionary["Population"] += all_states[state]["Population"]
		dictionary["Gross Domestic Product"] += all_states[state]["Gross Domestic Product"]
		dictionary["Gini Coefficient"] += float(all_states[state]["Gini Coefficient"])*float(all_states[state]["Population"])
		dictionary["Life Expectancy"] += float(all_states[state]["Life Expectancy"])*float(all_states[state]["Population"])
	dictionary["Population Density"] = round((float(dictionary["Population"])/float(dictionary["Area"])), 2)
	dictionary["Gini Coefficient"] = round(float(dictionary["Gini Coefficient"])/float(dictionary["Population"]), 2)
	dictionary["Life Expectancy"] = round(float(dictionary["Life Expectancy"])/float(dictionary["Population"]), 2)
	dictionary["GDP Per Capita"] = int(10**6*float(dictionary["Gross Domestic Product"])/float(dictionary["Population"]))
	dictionary = assign_ranks_and_similar(dictionary)
	return dictionary