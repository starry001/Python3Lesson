import json

d = dict(age=1, name='Bob', sex=1)
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d2 = json.loads(json_str)
print(d2)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


#
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
