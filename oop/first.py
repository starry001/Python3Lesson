

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.score = score

    def _print_(self):
        print('name:',self.__name,',score:',self.score)

s1 = Student('Bob',80)
s1._print_()

s2 = Student('Mike',90)
s2._print_()
print(s2._Student__name)
