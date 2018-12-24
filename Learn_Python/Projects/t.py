import psycopg2 as pg2
conn = pg2.connect(host='localhost', port='5432', 
                    database='appdb', user='mif', 
                    password='suncher85')
cur = conn.cursor()
cur.execute('SELECT * FROM greeting')
rows = cur.fetchall()
for row in rows:
    print (row[0])

conn.close()