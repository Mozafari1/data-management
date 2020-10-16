import csv
import geoip2.database
import time
start = time.time()
reader = geoip2.database.Reader(
    './GeoLite2-City_20201013/GeoLite2-City.mmdb')
#ips = []
with open('r-file.csv', newline='') as r_file:
    data = csv.DictReader(r_file)
    for row in data:
        # ips.append(row['ip'])
        response = reader.city(row['ip'])

        print('Country Iso_code:  {}'.format(response.country.iso_code))
        print('Country Name:      {}'.format(response.country.name))
        print('City:              {}'.format(response.city.name))
        print('Postal Code:       {}'.format(response.postal.code))
        print('Latitude:          {}'.format(response.location.latitude))
        print('Longitude:         {}'.format(response.location.longitude))
        print('IP Version:        {}'.format(response.traits.network))
        print('Continent        {}'.format(response.continent.name))
        print('\n')

done = time.time()
timeUsed = done - start

print(timeUsed)
