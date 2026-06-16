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
