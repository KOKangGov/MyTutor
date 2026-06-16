# itemgetter1.py

from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)


# dictionary 일 경우
from operator import itemgetter

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"neme": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 19, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)


# operator.attrgetter()

from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student('{self.name}', '{self.age}', '{self.grade}')"
    
students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('grade', 'age'))
print(result)
