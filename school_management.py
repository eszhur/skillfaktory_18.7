import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# сгенерируем данные по оценкам:
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks


def print_menu():
    print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить оценки ученика по предмету
5. Редактировать оценки ученика по предмету
6. Вывести все оценки для определенного ученика
7. Вывести средний балл по каждому предмету для определенного ученика
8. Добавить нового ученика
9. Добавить новый предмет
10. Удалить ученика
11. Удалить предмет
12. Выход из программы
''')


def add_grade():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    try:
        mark = int(input('Введите оценку: '))
    except ValueError:
        print("Ошибка: оценка должна быть числом.")
        return

    if student in students_marks and class_ in students_marks[student]:
        students_marks[student][class_].append(mark)
        print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')


def print_avg_grades():
    for student in students:
        print(student)
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            average = marks_sum / marks_count
            print(f'{class_} - {average:.2f}')
        print()


def print_all_grades():
    for student in students:
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()


def delete_grade():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    if student in students_marks and class_ in students_marks[student]:
        try:
            mark = int(input('Введите оценку для удаления: '))
            students_marks[student][class_].remove(mark)
            print(f'Оценка {mark} удалена для {student} по предмету {class_}')
        except ValueError:
            print("Ошибка: оценка должна быть числом.")
        except:
            print("Ошибка: оценка не найдена.")
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')


def edit_grade():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    if student in students_marks and class_ in students_marks[student]:
        try:
            old_mark = int(input('Введите оценку для замены: '))
            new_mark = int(input('Введите новую оценку: '))
            index = students_marks[student][class_].index(old_mark)
            students_marks[student][class_][index] = new_mark
            print(f'Оценка {old_mark} заменена на {new_mark} для {student} по предмету {class_}')
        except ValueError:
            print("Ошибка: оценка должна быть числом.")
        except:
            print("Ошибка: оценка не найдена.")
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')


def print_student_grades():
    student = input('Введите имя ученика: ')
    if student in students_marks:
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()
    else:
        print('ОШИБКА: неверное имя ученика')


def print_student_avg_grades():
    student = input('Введите имя ученика: ')
    if student in students_marks:
        print(student)
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            average = marks_sum / marks_count
            print(f'{class_} - {average:.2f}')
        print()
    else:
        print('ОШИБКА: неверное имя ученика')


def add_student():
    student = input('Введите имя нового ученика: ')
    if student not in students_marks:
        students.append(student)
        students.sort()
        students_marks[student] = {}
        for class_ in classes:
            students_marks[student][class_] = []
        print(f'Ученик {student} добавлен.')
    else:
        print('ОШИБКА: ученик уже существует')


def add_class():
    class_ = input('Введите название нового предмета: ')
    if class_ not in classes:
        classes.append(class_)
        for student in students_marks:
            students_marks[student][class_] = []
        print(f'Предмет {class_} добавлен.')
    else:
        print('ОШИБКА: предмет уже существует')


def delete_student():
    student = input('Введите имя ученика для удаления: ')
    if student in students_marks:
        students.remove(student)
        del students_marks[student]
        print(f'Ученик {student} удален.')
    else:
        print('ОШИБКА: ученик не найден')


def delete_class():
    class_ = input('Введите название предмета для удаления: ')
    if class_ in classes:
        classes.remove(class_)
        for student in students_marks:
            del students_marks[student][class_]
        print(f'Предмет {class_} удален.')
    else:
        print('ОШИБКА: предмет не найден')


while True:
    print_menu()
    try:
        command = int(input('Введите команду: '))
    except ValueError:
        print("Ошибка: команда должна быть числом.")
        continue

    if command == 1:
        add_grade()
    elif command == 2:
        print_avg_grades()
    elif command == 3:
        print_all_grades()
    elif command == 4:
        delete_grade()
    elif command == 5:
        edit_grade()
    elif command == 6:
        print_student_grades()
    elif command == 7:
        print_student_avg_grades()
    elif command == 8:
        add_student()
    elif command == 9:
        add_class()
    elif command == 10:
        delete_student()
    elif command == 11:
        delete_class()
    elif command == 12:
        print('Выход из программы')
        break
    else:
        print('ОШИБКА: неверная команда')
