import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


import numpy as np
is_threat_lis = []
is_threat = []
is_threat_dic = {}

is_attacker_lis = []
is_attacker = []
is_attacker_dic = {}

is_abuser_lis = []
is_abuser = []
is_abuser_dic = {}

is_tor_lis = []
is_tor = []
is_tor_dic = {}

same_ip_list = []
same_ip = []
same_ip_dic = {}

diff_is_threat_list = []
diff_is_threat = []
diff_is_threat_dic = {}


with open('data_with_date.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    with open('is_tor_ip.csv', 'w', encoding="utf-8", newline='')as wf:
        # , 'is_threat', 'diff_is_threat','is_known_attacker', 'is_known_abuser', 'is_tor']
        fieldnames = ['country', 'city', 'perform', 'latitude',
                      'longitude', 'is_known_attacker']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:

            # not all four  row['is_threat']=='True' and row['is_known_attacker']=='True' and row['is_known_abuser']=='True'and row['is_tor']=='True'
            # not row['is_threat']=='True' and row['is_known_attacker']=='True' and row['is_known_abuser']=='True'

            if (row['is_threat'] == 'True' and row['is_known_attacker'] == 'True' and row['is_tor'] == 'True'):
                same_ip_list.append(row['is_threat'])
                # writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                #                 'latitude': row['latitude'], 'longitude': row['longitude'], 'threat_and_attacker_and_tor_ip': row['ip']})

            if (row['is_threat'] == 'True' and row['is_known_attacker'] == 'False' and row['is_tor'] == 'False' and row['is_known_abuser'] == 'False'):
                diff_is_threat_list.append(row['is_threat'])
                # writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                #                  'latitude': row['latitude'], 'longitude': row['longitude'], 'diff_is_threat': row['ip']})

            if (row['is_threat'] == 'True'):
                is_threat_lis.append(row['is_threat'])

                # writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                #                  'latitude': row['latitude'], 'longitude': row['longitude'], 'is_threat': row['ip']})

            if (row['is_known_attacker'] == 'True'):
                is_attacker_lis.append(row['is_known_attacker'])
                writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                                 'latitude': row['latitude'], 'longitude': row['longitude'], 'is_known_attacker': row['ip']})
            if (row['is_known_abuser'] == 'True'):
                is_abuser_lis.append(row['is_known_abuser'])
                # writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                #                  'latitude': row['latitude'], 'longitude': row['longitude'], 'is_known_abuser': row['ip']})
            if (row['is_tor'] == 'True'):
                is_tor_lis.append(row['is_tor'])
                # writer.writerow({'country': row['country'], 'city': row['city'], 'perform': row['perform'],
                #                  'latitude': row['latitude'], 'longitude': row['longitude'], 'is_tor': row['ip']})


for i in is_threat_lis:
    is_threat_dic[i] = is_threat_dic.get(i, 0)+1

for i in is_attacker_lis:
    is_attacker_dic[i] = is_attacker_dic.get(i, 0)+1
for i in is_abuser_lis:
    is_abuser_dic[i] = is_abuser_dic.get(i, 0)+1
for i in is_tor_lis:
    is_tor_dic[i] = is_tor_dic.get(i, 0)+1
for i in same_ip_list:
    same_ip_dic[i] = same_ip_dic.get(i, 0)+1
for i in diff_is_threat_list:
    diff_is_threat_dic[i] = diff_is_threat_dic.get(i, 0)+1

for m, n in is_threat_dic.items():
    if(m == 'True'):
        is_threat.append(n)

for m, n in is_attacker_dic.items():
    if(m == 'True'):
        is_attacker.append(n)
for m, n in is_abuser_dic.items():

    if(m == 'True'):
        is_abuser.append(n)

for m, n in is_tor_dic.items():
    if(m == 'True'):
        is_tor.append(n)
for m, n in same_ip_dic.items():
    if(m == 'True'):
        same_ip.append(n)

for m, n in diff_is_threat_dic.items():
    if(m == 'True'):
        diff_is_threat.append(n)

print('same ip ', same_ip_dic)
print('is_threat ', is_threat_dic)
print('diff is threat ', diff_is_threat_dic)

print('is_attacker ', is_attacker_dic)
print('is_abuser ', is_abuser_dic)
print('is_tor ', is_tor_dic)

print('-----------------------------------------')
print('same ip ', same_ip)
print('is_threat ', is_threat)
print('dif_is_threat ', diff_is_threat)
print('is_attacker ', is_attacker)
print('is_abuser ', is_abuser)
print('is_tor ', is_tor)
l = 1
x = np.arange(l)  # the label locations
width = 0.1  # the width of the bars

fig, ax = plt.subplots(figsize=(4.7, 3.8))
rects2 = ax.bar(x, is_threat, width, label='is_threat')
rects1 = ax.bar(x + width, is_attacker, width, label='is_known_attacker')
rects1 = ax.bar(x + width+width, is_abuser, width, label='is_known_abuser')
rects1 = ax.bar(x + width+width+width, is_tor, width, label='is_tor')
rects1 = ax.bar(x + width+width+width+width, same_ip, width, label='same_ip')
rects1 = ax.bar(x + width+width+width+width+width,
                diff_is_threat, width, label='diff_is_threat')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of IPs')
ax.set_title('Shows what kind of threats ')
ax.set_xticks(x)
ax.set_xlabel("True")
ax.legend()
plt.savefig("pgf_fonts.png")

plt.show()
