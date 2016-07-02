import mysql.connector

conn = mysql.connector.connect(user='root', password='wangzhen', database='test')

cursor = conn.cursor()

# cursor.execute('create table user3 (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user3 (id, name) values (%s, %s)', ['1', 'Bob'])
print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()
