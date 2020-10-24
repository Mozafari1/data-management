import csv
import pandas as pd
import matplotlib.pyplot as plt

ips = []
num = []
data = {'ip': ips, 'number': num}
with open('r-file.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:

        ips.append(row['ip'])
        num.append(int(row['number']))

df = pd.DataFrame(data, columns=['ip', 'number'])

print(df)
df.plot(x='ip', y='number', kind='bar')
plt.show()
