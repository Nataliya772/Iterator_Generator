import hashlib

def generator_hash(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            hash = hashlib.md5(line.encode('utf-8')).hexdigest()
            yield hash


if __name__ == '__main__':
    for hash in generator_hash('country_link.txt'):
        print(hash)