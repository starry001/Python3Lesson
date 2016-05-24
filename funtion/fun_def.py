import math
import os
import itertools
from collections import Iterator
from functools import reduce


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(10, 10, 200, math.pi / 6)
print('x = %f,y = %f' % (x, y))
r = move(100, 100, 60, math.pi / 6)
print(r)


def my_sqrt(a, b, c):
    s = b * b - 4 * a * c
    x1 = ((-1 * b) + math.sqrt(s)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(s)) / (2 * a)
    return x1, x2


result = my_sqrt(1, -2, -3)
print(result)


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
t = (1, 2)
print(calc(*t))


# 关键字参数
def per(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


dict = {"1": 1, '2': '2'}
per('bob', 13, **dict)


def move(n, a, b, c, num=[1]):
    if n == 0:
        return

    move(n - 1, a, c, b, num)
    print('%d: %s --> %s' % (num[0], a, c))
    num[0] = num[0] + 1
    move(n - 1, b, a, c, num)


move(3, 'A', 'B', 'C')

# slince

L = [0, 1, 2, 3, 4]
print(L[-1:-6:-1])

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# ------
l = [d for d in os.listdir('..')]
print(l)

L = ['Hello', 'World', 18, 'Apple', None]
ll = [s.lower() for s in L if isinstance(s, str)]
print(ll)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + ' = ' + v for k, v in d.items()])
g = (x * x for x in range(11))
print(g)
for v in g:
    print(v)


# Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(5)
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
print(list(itertools.permutations(horses)))

# Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance(100, Iterator))
print(isinstance(str, Iterator))
print(isinstance((x for x in range(11)), Iterator))
print(isinstance([x for x in range(11)], Iterator))

i = iter([])
print(i)
print(isinstance(i, Iterator))


# high funtion
def same(x, *fs):
    s = [f(x) for f in fs]
    return s


print(same(2, math.sqrt, abs))

# map
list = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list)


# reduce
def my_sum(x, y):
    return x + y


s = reduce(my_sum, [1, 3, 5, 7, 9])
print(s)


def int2num(x, y):
    return 10 * x + y


num = reduce(int2num, [1, 3, 5, 7, 9])
print(num)


# test
def normalstr(name):
    return str.capitalize(name)


names = ['adam', 'LISA', 'barT']
for name in names:
    print(normalstr(name))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('1 * 3 * 5 * 7 = ', prod([1, 3, 5, 7]))
s = '123.456'
sn = s.split('.')[0] + s.split('.')[1]
print(sn)


def returnNum():
    for i in range(10, 100):
        if str(i)[::-1] == str(i):
            print(i)


returnNum()

print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0])

L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L2, reverse=True))


def by_name(t):
    return t[0]


l = sorted(L, key=by_name)
print(l)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1 = count()
print(f1)

def now():
    print("----")

f = now
f()
print(f.__name__)

def nn(*nums):
    print(nums)

l = [1,2,3]
nn(*l)

args = [10, 5, 6, 7]
print(max(*args))
