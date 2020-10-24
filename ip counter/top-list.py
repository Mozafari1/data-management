import csv
ips = []

with open('country_list.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(int(row['number']))
        if(int(row['number']) >= 1853):
            print(row['country'], '&', row['number'])
            pass
        else:
            pass
ips.sort()
print(ips[-5:])
