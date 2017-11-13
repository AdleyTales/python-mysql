import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='root')

cursor = conn.cursor()

# create database my_data
cursor.execute('create database if not exists my_data ')

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
