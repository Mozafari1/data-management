import csv
with open('fixed_data.csv', encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    with open('./threat_info/threat_info.csv', 'w', encoding="utf-8", newline='')as wf:
        fieldnames = ['is_anonymous', 'is_bogon',
                      'is_known_abuser', 'is_known_attacker', 'is_proxy', 'is_threat', 'is_tor', 'ip', 'datetime']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:

            writer.writerow({'is_anonymous': row['is_anonymous'], 'is_bogon': row['is_bogon'], 'is_known_abuser': row['is_known_abuser'],
                             'is_known_attacker': row['is_known_attacker'], 'is_proxy': row['is_proxy'], 'is_threat': row['is_threat'], 'is_tor': row['is_tor'], 'ip': row['ip'], 'datetime': row['datetime']})


# COPY countries(country_name, country_code, calling_code, continent_id)
# FROM 'C:\Program Files\PostgreSQL\13\bin\output.csv'
# DELIMITER ','
# CSV HEADER;
