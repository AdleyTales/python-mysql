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
cursor.execute('delete from my_table where id = 3243')

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
