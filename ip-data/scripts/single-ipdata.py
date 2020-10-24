from ipdata import ipdata
from pprint import pprint
#
# Create an instance of an ipdata object. Replace `test` with your API Key
token = 'your token key'
ipdata = ipdata.IPData(token)
ips = ['106.13.182.60',
       # '49.234.10.207',
       #   '120.31.138.70',
       #    '112.85.42.185',
       #    '157.230.47.57',
       #    '119.57.120.107',
       #    '113.108.168.215',
       #    '120.98.1.180',
       #    '83.56.44.200',
       #    '119.226.11.100',
       #    '104.248.246.8',
       '37.213.204.135']
l = []
for i in ips:

    response = ipdata.lookup(i, fields=['ip',
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
    l.append(response)
    #print(i, "={}".format(response))
print(l)
