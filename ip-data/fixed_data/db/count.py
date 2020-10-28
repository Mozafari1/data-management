import csv
ips = []
dictonary = {}

with open('./threat_info/threat_info.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['is_tor'])
        # ips.append(row['ip'])

for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1

with open('./threat_info/is_tor.csv',  'w', encoding="utf-8", newline='')as wf:
    fieldnames = ['type']
    writer = csv.DictWriter(wf, fieldnames=fieldnames)
    writer.writeheader()
    for m, n in dictonary.items():
        writer.writerow({'type': '%s' % m
                         })
