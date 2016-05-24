print("hello world");
# a = input('please input a munber:')
# a = int(a)
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# age = input("please input a age:")
# age = int(age)
# if age > 18:
#     print(">18")
# else:
#     print("<=18")

print('1 \'am \"ok\"!');
print('''line1
... line2
... line3''')
print(2 > 3)

print(ord("A"))
print(chr(65))
print(ord('中'))
print(chr(20013))
print('abc'.encode('ascii'))
print(len("中文"))
print(len('中文'.encode('utf-8')))

print('Hello, %s' % 'world')
print('%2d-%03d' % (3, 1))

s1 = 72
s2 = 85
rate = (s2 - s1) / s1 * 100
print("提升比:%.2f%%" % rate)

classmate = ['a', 'b', 'c']
print(classmate)
print(classmate[-3])
classmate.append('d')
print(classmate[-1])
classmate.pop()
print(classmate)
classmate.insert(2, 'e')
print(classmate)
t = (1,)
print(t)

list1 = ['Apple', 'Google', 'Microsoft']
list2 = ['Java', 'Python', 'Ruby', 'PHP']
list3 = ['Adam', 'Bart', 'Lisa']

tt = (list1, list2, list3)
print(tt[0][0])
print(tt[1][1])
print(tt[2][2])
L = ['Bart', 'Lisa', 'Adam']
for n in L:
    print('Hello:%s' % n)

# dist
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Bob'] = 70
print(d)
result = d.get('aa', -11)
print(result)
# print('ab'in d)
n1 = 255
n2 = 1000
a = hex(255)
print(a)
print(isinstance(a, str))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(1.2))
