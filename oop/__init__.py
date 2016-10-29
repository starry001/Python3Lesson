class MyClass:
    @staticmethod
    def smeth():
        print('this is static method')

    @classmethod
    def cmeth(self):
        print('this is a class method of %s', self)


MyClass.cmeth()
MyClass.smeth()

my = MyClass()
my.cmeth()
