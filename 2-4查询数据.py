import mysql.connector

config = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'my_data'
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

# insert data
cursor.execute('select * from my_table where id = 1002')

print(cursor.rowcount)

values = cursor.fetchall()

print(values)

conn.commit()
cursor.close()
conn.close()
