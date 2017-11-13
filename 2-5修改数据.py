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
cursor.execute('update my_table set password = "ceshipwd" where id = 121')

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
