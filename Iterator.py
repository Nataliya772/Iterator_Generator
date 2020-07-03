import os
from list_countries import get_list_countries


class CountriesIterator:

    def __init__(self, list_path, file_path):
        self.list_path = list_path
        self.index = -1
        self.end = len(list_path)
        self.element = ''
        self.link = 'https://en.wikipedia.org/wiki/'
        self.file_output = open(file_path, 'w', encoding='utf-8')


    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.end:
            self.element = f'{self.list_path[self.index]} - {self.link + self.list_path[self.index]}'
            self.file_output.write(self.element + os.linesep)
        if self.index == self.end:
            raise StopIteration
        return self.element
        self.file_output.close()


if __name__ == '__main__':
    for item in CountriesIterator(get_list_countries(), 'country_link.txt'):
        print(item)