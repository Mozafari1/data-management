import csv
Path_file = '../fixed_data/'
mith_path_file = 'continents'
input_path_file = Path_file+mith_path_file + '/continents_list.csv'
ips = []
dictonary = {}


def read_file():
    with open(Path_file+'fixed_data.csv', encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ips.append(row['continent'])
            ips.append(row['continent_code'])


def counter():
    for i in ips:
        dictonary[i] = dictonary.get(i, 0)+1


def write_file():
    with open(input_path_file,  'w', encoding="utf-8", newline='')as wf:
        fieldnames = ['continent', 'continent_code']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for m, n in dictonary.items():
            writer.writerow({'continent': '%s' % m, 'continent_code': '%s' % n
                             })


if __name__ == "__main__":
    read_file()
    counter()
    write_file()
