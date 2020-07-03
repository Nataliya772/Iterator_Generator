import requests


def get_list_countries():
    URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    Response = requests.get(URL)
    rj = Response.json()
    list_countries = []
    for country in rj:
        official_name = country['name']['official']
        name = official_name.split()
        country_name = '_'.join(name)
        list_countries.append(country_name)
    return list_countries

