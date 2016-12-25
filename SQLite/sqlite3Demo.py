import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test2.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key , name varchar(20))')
print(cursor.description)

cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
print(cursor.description)
print(cursor.rowcount)

cursor.execute('select *from user where id = \'1\'')
print(cursor.description)

cursor.close()
conn.commit()
conn.close()
