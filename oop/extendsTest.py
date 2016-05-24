class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')


dog = Dog()
dog.run()

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Animal))


class Timer(object):
    def run(self):
        print('Start...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Timer())

print(type(123))
print(type(Dog()))
print(type(abs))

print(dir('abc'))


class A(object):
    name = 'a'


a = A()
print(a.name)
print(A.name)
a.name = 'b'
print(a.name)
del a.name
print(a.name)
