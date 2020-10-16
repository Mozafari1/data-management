import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def printRecord(ip):
    rec = gi.record_by_name(ip)
    country_code = rec['country_code']
    continent = rec['continent']
    region_code = rec['region_code']
    time_zone = rec['time_zone']
    city = rec['city']
    country = rec['country_name']
    longitude = rec['longitude']
    lat = rec['latitude']

    print('[+] IP-Address: ' + ip + ' Geo-located ')
    print('[+] City: ' + str(city) + ', Country: '+str(country))
    print('[+] Country Code: ' + str(country_code) +
          ' , Continent: '+str(continent))
    print('[+] Region Code: ' + str(region_code) +
          ' , Time Zone: ' + str(time_zone))
    print('[+] Latitude: ' + str(lat) + ', Longitude: ' + str(longitude))


l = ['1.36.57.85']  # 10.36.57.85 => 4

for ip in l:
    if (ip == 'None'):
        print('None')
    printRecord(ip)
