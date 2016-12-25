from cumulation.models import Country
import pandas as pd 
import numpy as np 

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
	c.total_population = dictionary["Population"]
	c.population_density = dictionary["Population Density"]
	c.gdp_total = dictionary["Gross Domestic Product"]
	c.gdp_per_capita = dictionary["GDP Per Capita"]
	c.gini = dictionary["Gini Coefficient"]
	c.life_expectancy = dictionary["Life Expectancy"]
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
def process_states(states_array):
	all_states = read_excel("cumulation/static/spreadsheets/states_data.xls")
	
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
	return dictionary