import csv
from ipdata import ipdata
from pprint import pprint
token = 'your token key'
ipdata = ipdata.IPData(token)
ips = []
file1 = open("2.txt", "w", encoding="utf-8", newline='')

with open('wf.csv', encoding="utf-8", newline='') as rf:
    data = csv.DictReader(rf)

    for row in data:
        response = ipdata.lookup(row['ip'], fields=['ip',
                                                    'asn',
                                                    'calling_code',
                                                    'city',
                                                    'continent_code',
                                                    'continent_name',
                                                    'country_code',
                                                    'country_name',
                                                    'is_eu',
                                                    'latitude',
                                                    'longitude',
                                                    'postal',
                                                    'region',
                                                    'region_code',
                                                    'status',
                                                    'threat'

                                                    ]
                                 )
        ips.append(response)
        file1.writelines(str(response))

file1.close()
