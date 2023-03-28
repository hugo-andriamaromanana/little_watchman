from bs4 import BeautifulSoup
import json

with open('countries.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')

parsed = {}

all_countries = soup("h3", "country-name")
all_capitals = soup("span", "country-capital")
all_populations = soup("span", "country-population")
all_areas = soup("span", "country-area")

for i in range(len(all_countries)):
    parsed[(all_countries[i].text.strip()).replace('\n', '')] = {
        "Capital": all_capitals[i].text,
        "Population": all_populations[i].text,
        "Area (km2)": all_areas[i].text
    }

with open('countries.json', 'w') as fp:
    json.dump(parsed, fp, indent=4)
