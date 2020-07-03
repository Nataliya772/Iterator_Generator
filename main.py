from Iterator import CountriesIterator
from generator import generator_hash
from list_countries import get_list_countries


if __name__ == '__main__':
    for item in CountriesIterator(get_list_countries(), 'country_link.txt'):
        print(item)
    for hash in generator_hash('country_link.txt'):
        print(hash)
