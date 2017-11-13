# python 操作 mysql
>- 众所周知，mysql是非常出名的关系型数据库。
>- 本文使用的是python3.6 version

## 第一步：需要安装mysql数据库

## 第二步：下载python驱动包

```py

  pip3 install mysql-connector==2.1.4

```
** 注意一下：**

- 注意： 默认安装mysql-connector 会失败，失败的原因是这个驱动包默认是测试版本，需要指定2.1.4

- 廖雪峰的python教程这个地方有个坑，按照教程安装这个驱动包会一直报错。解决办法就是指定驱动包的版本号。

## 2.1 创建数据库

    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='root')

    cursor = conn.cursor()

    # create database my_data
    cursor.execute('create database if not exists my_data ')

    print(cursor.rowcount)

    conn.commit()
    cursor.close()
    conn.close()

## 2.2 创建数据表

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

## 2.3 插入数据 insert

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

## 查询数据 select

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

## 修改数据 update

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

## 删除数据 delete

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
