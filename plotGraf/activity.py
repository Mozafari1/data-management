import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
ips = []
dictonary = {}

with open('data_with_date.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ips.append(row['ip'])

for i in ips:
    dictonary[i] = dictonary.get(i, 0)+1
# print(len(dictonary))

fig, axs = plt.subplots(3, 2, figsize=(30, 5), sharey=False, sharex=False)

fig.suptitle('Shows the activity of each IP Addresses', fontsize='large')


for m, n in dictonary.items():
    if(n < 5):
        axs[0, 0].bar(x=m, height=n)
    elif(n > 5 and n < 9):
        axs[0, 1].bar(x=m, height=n)
    elif(n > 9 and n < 15):
        axs[1, 0].bar(x=m, height=n)
    elif(n > 15 and n < 26):
        axs[1, 1].bar(x=m, height=n)
    elif(n > 26 and n < 70):
        axs[2, 0].bar(x=m, height=n)
    elif(n > 70):
        axs[2, 1].bar(x=m, height=n)


fig.autofmt_xdate(rotation=90)
fig.suptitle('Shows the activity of each IP Addresses', fontsize='large')


fig.text(0.06, 0.5, 'Number of activity', ha='center',
         va='center', rotation='vertical')

fig.autofmt_xdate(rotation=90)


plt.show()
