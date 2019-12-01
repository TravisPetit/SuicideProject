import psycopg2

conn = psycopg2.connect(
	host="localhost",
	user="postgres",
        database="postgres",
	password="123"
        )

cursor = conn.cursor()
cursor.execute("SET search_path TO suicide_schema")


cursor.execute('INSERT INTO "Action" \
(id, eventCode, eventRootCode, eventBaseCode, isRootEvent, quadClass, goldsteinScale, avgTone)\
VALUES \
(1,  123,       456,           789,            101112,      2,         15,              54)')

cursor.execute('SELECT * FROM "Action"')
rows = cursor.fetchall()

for r in rows:
    print(r)

cursor.close()
conn.close()
