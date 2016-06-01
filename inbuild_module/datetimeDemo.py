from datetime import datetime, timedelta

'''
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

如果仅导入import datetime，则必须引用全名datetime.datetime。

datetime.now()返回当前日期和时间，其类型是datetime。
'''
now = datetime.now()
print(now)
print(type(now))

# 用指定时间创建datetime
# 注意转换后的datetime是没有时区信息的。
dt = datetime(2014, 10, 22, 10, 20, 30, 123)
print(dt)

# str to datetime
strdate = datetime.strptime("2014-10-22 10:20:30", "%Y-%m-%d %H:%M:%S")
print(strdate)

# datetime to str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(type(now))

# 时间加减
now = datetime.now()
print(now)
now = now + timedelta(hours=3)
print(now)
now = now - timedelta(days=2)
print(now)
