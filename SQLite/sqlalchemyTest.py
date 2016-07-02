'''
第三方ORM框架sqlalchemy使用
'''

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

##创建对象基类

Base = declarative_base()


class User(Base):
    ## table name
    __tablename__ = 'user'

    ##表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


##初始化数据库连接
##SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:wangzhen@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

##关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
session = DBSession()
new_user = User(id='5', name='starry5')
session.add(new_user)
session.commit()
session.close()

##查询
session = DBSession()
##创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '4').one()
print('type:', type(user))
print('name:', user.name)
session.close()
