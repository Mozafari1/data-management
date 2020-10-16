import csv
import geoip2.database
import time
Path_db = '../GeoLite2-City_20201013/GeoLite2-City.mmdb'
Path_csv = '../csv/'
Path_log = '../log/log.log'

start = time.time()

reader = geoip2.database.Reader(Path_db)
with open(Path_csv+'final.csv', encoding="utf-8", newline='') as rf:
    data = csv.DictReader(rf)
    with open(Path_csv+'ip_location', 'w', encoding="utf-8", newline='')as wf:
        fieldnames = [
            'date_1',
            'action',
            'server_port',
            'message',
            'ssh',
            'perform',
            'ip',
            'continent',
            'country_iso_code',
            'country_name',
            'city',
            'postal_code',
            'latitude',
            'longitude',
            'ip_version',
            'date_2'
        ]
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            response = reader.city(row['ip'])

            writer.writerow(
                {
                    'date_1': row['date_1'],
                    'action': row['action'],
                    'server_port': row['server_port'],
                    'message': row['message'],
                    'ssh':  row['ssh'],
                    'perform':  row['perform'],
                    'ip':  row['ip'],
                    'continent': '{}'.format(response.continent.name),
                    'country_iso_code': '{}'.format(response.country.iso_code),
                    'country_name': '{}'.format(response.country.name),
                    'city': '{}'.format(response.city.name),
                    'postal_code': '{}'.format(response.postal.code),
                    'latitude': '{}'.format(response.location.latitude),
                    'longitude': '{}'.format(response.location.longitude),
                    'ip_version': '{}'.format(response.traits.network),
                    'date_2': row['date_2']
                }
            )

done = time.time()
timeUsed = done - start
print(timeUsed)
