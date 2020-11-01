import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


import numpy as np
country_lis = []
country = []
country_dic = {}

ip_lis = []
ip = []
ip_dic = {}

perform_lis = []
perform = []
perform_dic = {}


with open('is_known_abuser_ip2.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        country.append(row['country'])
        ip.append(row['ip'])
        perform.append('perform')

for i in country_lis:
    country_dic[i] = country_dic.get(i, 0)+1

for i in ip_lis:
    ip_dic[i] = ip_dic.get(i, 0)+1
for i in perform_lis:
    perform_dic[i] = perform_dic.get(i, 0)+1


for m, n in country_dic.items():
    country.append(n)

for m, n in ip_dic.items():
    ip.append(n)
for m, n in perform_dic.items():

    perform.append(n)

x = np.arange(1)  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, country, width, label='ip')
rects2 = ax.bar(x + width/2, country, width, label='country')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.legend()

plt.xticks(rotation=90)
plt.show()
