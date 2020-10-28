import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="data-management",
    user="postgres",
    password="postgreSQL"

)
cur = conn.cursor()
# execute query
cur.execute("SELECT  cities.city_id,cities.city_name, cities.country_id FROM cities INNER JOIN countries ON cities.country_id=countries.country_id WHERE city_name='Oslo';")
rows = cur.fetchall()
for r in rows:
    print(f"city_id {r[0]} city_name {r[1]} country_id {r[2]}")
cur.close()
conn.close()
