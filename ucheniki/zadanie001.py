import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']

students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

def print_commands():
    print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить оценку ученика по предмету
5. Редактировать оценку ученика по предмету
6. Вывести все оценки определенного ученика
7. Вывести средний балл по каждому предмету определенного ученика
8. Добавить нового ученика
9. Удалить ученика
10. Добавить новый предмет
11. Удалить предмет
12. Выход из программы
''')

print_commands()

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum / marks_count:.2f}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку для удаления: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Оценка {mark} для {student} по предмету {class_} удалена')
            else:
                print('ОШИБКА: у ученика нет такой оценки по указанному предмету')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        old_mark = int(input('Введите оценку для редактирования: '))
        new_mark = int(input('Введите новую оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if old_mark in students_marks[student][class_]:
                idx = students_marks[student][class_].index(old_mark)
                students_marks[student][class_][idx] = new_mark
                print(f'Оценка {old_mark} для {student} по предмету {class_} изменена на {new_mark}')
            else:
                print('ОШИБКА: у ученика нет такой оценки по указанному предмету')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 6:
        print('6. Вывести все оценки определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 7:
        print('7. Вывести средний балл по каждому предмету определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum / marks_count:.2f}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 8:
        print('8. Добавить нового ученика')
        student = input('Введите имя нового ученика: ')
        if student not in students_marks.keys():
            students_marks[student] = {class_: [] for class_ in classes}
            students.append(student)
            students.sort()
            print(f'Ученик {student} добавлен')
        else:
            print('ОШИБКА: ученик уже существует')
    elif command == 9:
        print('9. Удалить ученика')
        student = input('Введите имя ученика для удаления: ')
        if student in students_marks.keys():
            del students_marks[student]
            students.remove(student)
            print(f'Ученик {student} удалён')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 10:
        print('10. Добавить новый предмет')
        class_ = input('Введите название нового предмета: ')
        if class_ not in classes:
            classes.append(class_)
            for student in students_marks.keys():
                students_marks[student][class_] = []
            print(f'Предмет {class_} добавлен')
        else:
            print('ОШИБКА: предмет уже существует')
    elif command == 11:
        print('11. Удалить предмет')
        class_ = input('Введите название предмета для удаления: ')
        if class_ in classes:
            classes.remove(class_)
            for student in students_marks.keys():
                del students_marks[student][class_]
            print(f'Предмет {class_} удалён')
        else:
            print('ОШИБКА: предмет не существует')
    elif command == 12:
        print('12. Выход из программы')
        break
    else:
        print('ОШИБКА: неверная команда')
        print_commands()
