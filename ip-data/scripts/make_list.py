import csv
Path_file = '../fixed_data/'
mith_path_file = 'countries'
input_path_file = Path_file+mith_path_file + '/country_list.csv'
ips = []
dictonary = {}


def read_file():
    with open(Path_file+'fixed_data.csv', encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ips.append(row['country'])


def counter():
    for i in ips:
        dictonary[i] = dictonary.get(i, 0)+1


def write_file():
    with open(input_path_file,  'w', encoding="utf-8", newline='')as wf:
        fieldnames = ['country', 'number']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for m, n in dictonary.items():
            writer.writerow({'country': '%s' % m, 'number': '%s' % n
                             })


if __name__ == "__main__":
    read_file()
    counter()
    write_file()
