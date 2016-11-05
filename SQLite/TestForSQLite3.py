import os
import sqlite3

# conn = sqlite3.connect('test.db')
#
# cursor = conn.cursor()
# cursor.execute('select * from user where id = 1')
#
# # 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。
# # 结果集是一个list，每个元素都是一个tuple，对应一行记录。
# values = cursor.fetchall()
# print(values)
#
# cursor.close()
# conn.close()


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user2(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user2 values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user2 values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user2 values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name from user2 where score between ? and ? order by score', (low, high))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.commit()
    conn.close()


get_score_in(60, 100)
