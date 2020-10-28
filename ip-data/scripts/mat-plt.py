import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
ips = []
dictonary = {}

with open('../fixed_data/fixed_data.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['ip'])

for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1
print(len(dictonary))

fig, axs = plt.subplots(2, 2, figsize=(9, 4), sharey=True)


for m, n in dictonary.items():
    if(n < 2):
        axs[0, 0].bar(x=m, height=n)
    elif (n > 30 and n < 100):
        axs[0, 1].bar(x=m, height=n)
    elif(n > 10 and n < 30):
        axs[1, 0].bar(x=m, height=n)
    else:
        axs[1, 1].bar(x=m, height=n)

fig.autofmt_xdate(rotation=45)
plt.show()
