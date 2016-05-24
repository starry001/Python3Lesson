from types import MethodType
from enum import Enum, unique


class Student(object):
    pass


def set_age(self, age):
    self.age = age


s = Student()
s.name = 'Bob'
print(s.name)
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


# 给实例绑定方法对另一个实例不起作用
# s2 = Student()
# s2.set_age(10)
# print(s2.age)

def set_score(self, score):
    self.score = score


# 对类绑定方法对所有实例度有作用
Student.set_score = MethodType(set_score, Student)
s3 = Student()
s3.set_score(80)
print(s3.score)
s4 = Student()
s4.set_score(90)
print(s4.score)


class father(object):
    __slots__ = ('name', 'age')


f1 = father()
f1.name = 'f'
print(f1.name)


# error
# f1.s = 3
# print(f1.s)

class son(father):
    pass


s = son()
s.ss = 3
print(s.ss)

print('------------')


def set_age(self, age):
    self.age = age


class Stu(object):
    pass


Stu.set_age = MethodType(set_age, Stu)
A = Stu()
A.set_age(10)
print(A.age, id(A.age))
B = Stu()
B.set_age(15)
print(A.age, B.age, id(A.age), id(B.age))


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 10
print(s.score)


class screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be int type')
        if value <= 0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def hight(self):
        return self._hight

    @hight.setter
    def hight(self, value):
        if not isinstance(value, int):
            raise ValueError('hight must be int type')
        if value <= 0:
            raise ValueError('hight must be > 0')
        self._hight = value

    @property
    def solution(self):
        return self._hight * self._width


s = screen()
s.width = 1
print(s.width)
s.hight = 30
print(s.solution)


# 定制类
class Person(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'person \'name is %s' % self._name

    __repr__ = __str__


p = Person('BOb')
print(p)
p


class Fib(object):
    def __init__(self):
        self.x, self.y = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.x, self.y = self.y, self.x + self.y
        if self.x > 1000:
            raise StopIteration
        return self.x

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(x)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):
        if attr == 'name':
            return 'no attr name'
        return AttributeError('Fib() has no attr : %s' % attr)


for n in Fib():
    print(n)

f = Fib()
print(f[3])

l = list(range(100))[5:10]
print('-------------')
print(l)
print('--- f() slince----')
print(f[:10])
print(f.names)


# ---rest api --动态链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print('self._path:', self._path)
        print('path:', path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print('---rest api-----')
api = Chain().status.user.timeline.list
print(api)


class Po(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)


p = Po('aa')
p()

# ---enum
month = Enum('Month', ('mon', 'satu', 'wens', 'fir'))
for name, member in month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun.value)
print(Weekday(2))
for name, member in Weekday.__members__.items():
    print(name, '=>', member.value)


# type 
def h(self, name='hello'):
    print('name is %s' % name)


# 动态定义类
Hello = type('Hello', (object,), dict(hello=h))
h1 = Hello()
h1.hello()
print(type(Hello))
print(type(h))
