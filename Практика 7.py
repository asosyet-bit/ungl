from dataclasses import dataclass

@dataclass

class Student:
    name: str
    age: int
    major: str
    gpa: float

    def display_info(self):
        return (f'Имя студента:{self.name}, Возраст:{self.age}'
                f'Специальность:{self.major}, Средний балл:{self.gpa}')

    def calculate_grade(self):
        if self.gpa >= 4.5:
            return 'Отлично'
        elif self.gpa >= 3.5:
            return 'Хорошо'
        elif self.gpa >= 2.5:
            return 'Удовлетворительно'
        else:
            return 'Неудовлетворительно'


# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")

sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)

print('Отсортированный список студентов:')
for student in sorted_students:
    print(student.display_info())