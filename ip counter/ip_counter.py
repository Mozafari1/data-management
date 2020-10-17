import csv
ips = []
dictonary = {}

with open('r-file.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['ip'])
for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1

with open('w-file.csv',  'w', encoding="utf-8", newline='')as wf:
    fieldnames = ['ip', 'number']
    writer = csv.DictWriter(wf, fieldnames=fieldnames)
    writer.writeheader()
    for j, k in dictonary.items():
        writer.writerow({'ip': '%s' % j, 'number': '%s' % k})
