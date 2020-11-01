import csv
ips = []
dictonary = {}

with open('is_tor_ip.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['country'])
        # ips.append(row['ip'])

for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1
print(dictonary)
with open('count.csv',  'w', encoding="utf-8", newline='')as wf:
    fieldnames = ['country', 'number']
    writer = csv.DictWriter(wf, fieldnames=fieldnames)
    writer.writeheader()
    for m, n in dictonary.items():
        writer.writerow({'country': '%s' % m, 'number': '%s' % n
                         })
