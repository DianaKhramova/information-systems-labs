#coding:utf-8

groupmates = [
    {
        "name": u"Диана",
        "group": "bst2253",
        "age": 29,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Ольга",
        "group": "bst2253",
        "age": 23,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Игорь",
        "group": "bst2257",
        "age": 25,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Дмитрий",
        "group": "bst2257",
        "age": 26,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    for student in students:
        print student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20)
    print "\n"

def filter_students_by_avg_mark(students, min_avg):
    filtered = []
    for student in students:
        marks = student["marks"]
        avg_mark = sum(marks) / float(len(marks))
        if avg_mark > min_avg:
            filtered.append(student)
    return filtered

print_students(groupmates)

print u"Студенты со средним баллом выше 4.0:"
filtered = filter_students_by_avg_mark(groupmates, 4.0)
print_students(filtered)
