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
cursor.execute('insert into my_table (id,name,age) values (3243,"sunxiaohui",23)')

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
