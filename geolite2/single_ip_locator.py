import geoip2.database
reader = geoip2.database.Reader(
    './GeoLite2-City_20201013/GeoLite2-City.mmdb')

ips = ['62.234.15.136']

for i in ips:
    response = reader.city(i)

    print('{},'.format(response.continent.name)+'{},'.format(response.country.iso_code)
          + '{},'.format(response.country.name)+'{},'.format(response.city.name) +
          '{},'.format(response.postal.code)+'{},'.format(response.location.latitude) +
          '{},'.format(response.location.longitude)+'{},'.format(response.traits.network)+'\n')
