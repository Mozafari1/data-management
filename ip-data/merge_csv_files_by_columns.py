# import csv
# with open('data-csv.csv', 'data-2.csv', newline='') as f:
#     reader = csv.DictReader(f)
#     with open('w-file.csv', 'w', newline='')as wf:
#         fieldnames = ['date_1', 'ip', 'asn', 'name', 'domain', 'route', 'type', 'calling_code', 'city',
#                       'continent_code', 'continent_name', 'country_code', 'country_name', 'is_eu', 'latitude',
#                       'longitude', 'postal', 'region', 'region_code', 'is_tor', 'is_proxy', 'is_anonymous', 'is_known_attacker', 'is_known_abuser', 'is_threat', 'is_bogon', 'status']
#         writer = csv.DictWriter(wf, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in reader:
#             writer.writerow({'date_1': row['date_1'], 'ip': row['ip'], 'asn': row['asn'], 'name': row['name'], 'domain': row['domain'], 'route': row['route'], 'type': row['type'], 'calling_code': row['calling_code'], 'city': row['city'],
#                              'continent_code': row['continent_code'], 'continent_name': row['continent_name'], 'country_code': row['country_code'], 'country_name': row['country_name'], 'is_eu': row['is_eu'], 'latitude': row['latitude'],
#                              'longitude': row['longitude'], 'postal': row['postal'], 'region': row['region'], 'region_code': row['region_code'], 'is_tor': row['is_tor'], 'is_proxy': row['is_proxy'], 'is_anonymous': row['is_anonymous'],
#                              'is_known_attacker': row['is_known_attacker'], 'is_known_abuser': row['is_known_abuser'], 'is_threat': row['is_threat'], 'is_bogon': row['is_bogon'], 'status': row['status']})
contents = []

for filenum in range(2):
    f = open('data-{}.csv'.format(filenum + 1), 'r')
    lines = f.readlines()
    print(lines)
    f.close()

    if contents == []:
        contents = [[] for a in range(len(lines))]

    for row in range(len(lines)):
        contents[row].append(lines[row].rstrip('\n'))
        print(lines[row])

# print(contents)
f = open('merged.csv', 'w')

for row in range(len(contents)):
    line = str(contents[row])
    line = line.strip('[]')
    f.write(line + '\n')

f.close()
