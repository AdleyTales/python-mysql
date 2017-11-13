import mysql.connector

config = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'my_data'
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

# create table
cursor.execute('create table my_table (id int, name varchar(30), age int, password varchar(30)) ')

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
