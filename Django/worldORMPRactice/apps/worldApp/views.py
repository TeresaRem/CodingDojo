from django.shortcuts import render
from . import models

# Create your views here.
def index(req):
  # 1. countries that speak solvene
  # cities = models.Countries.objects.filter(languagetocountry__language='slovene')
  # languages = models.Languages.objects.filter(language='slovene')
  # prints the queries
  # print cities.query
  # print languages.query
  # context={'languages':languages,'cities':cities}
  # print context['languages']

  # 2. What query would you run to display the total number of cities for each country? 
  # Your query should return the name of the country and the total number of cities. 
  # You query should arrange the result by the number of cities in descending order.

  # SELECT countries.name, COUNT(cities.name)
  # FROM cities
  # JOIN countries ON countries.id = cities.country_id
  # GROUP BY country_id 
  # ORDER BY COUNT(cities.name) DESC

  # this works lol
  # countries = models.Cities.objects.raw('SELECT countries.name as id, COUNT(cities.ID) as count FROM cities JOIN countries ON countries.ID = cities.country_id GROUP BY country_id ORDER BY COUNT(cities.ID) DESC')
  # print countries.query

  # 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order.
  # countries = models.Cities.objects.raw('SELECT cities.name as id, cities.population as count FROM cities WHERE cities.country_code="MEX" ORDER BY cities.population DESC')

  # 4. i'm doing all these as SQL queries... lol

  context={'countries':countries}
  return render(req, 'worldApp/index.html', context)
# country.name,COUNT(cities.id)