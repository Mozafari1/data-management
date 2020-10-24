import csv
ips = []
dictonary = {}

with open('r-file.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['ip'])
        # ips.append(row['ip'])

print(ips)
for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1

with open('ip_list.csv',  'w', encoding="utf-8", newline='')as wf:
    fieldnames = ['ip', 'number']
    writer = csv.DictWriter(wf, fieldnames=fieldnames)
    writer.writeheader()
    for m, n in dictonary.items():
        writer.writerow({'ip': '%s' % m, 'number': '%s' % n
                         })

# 5 China
# 1 Ecuador
# 4 South Korea
# 1 France
# 1 Italy
