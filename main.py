
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average(self):
        self.average = [grade for grades in self.grades.values() for grade in grades]
        if self.average:
            self.averages = (sum(self.average) / len(self.average))
            return self.averages
        else:
            return ("Нет оценки")

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() == other.__average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() < other.__average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() > other.__average()


    def __str__(self):
        some_student = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашнее задание: {self.__average}\n' \
                       f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
                       f'Завершенные курсы: {self.finished_courses}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __average(self):
        self.average = [grade for grades in self.grades.values() for grade in grades]
        if self.average:
            self.averages = (sum(self.average) / len(self.average))
            return self.averages
        else:
            return ("Нет оценок")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() == other.__average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() < other.__average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() > other.__average()

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'Средняя оценка за лекцию: {self.__average}'
        return some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_reviewer


best_lecturer = Lecturer('Oleg', 'Bulygin')
best_lecturer.courses_attached += 'Python', 'Git', 'Java', 'HTML', 'C++'
lecturer = Lecturer('Anastasia', 'Bohan')
lecturer.courses_attached += 'Rehabilitation science', 'Pediatrician', 'Exercise therapy'



best_student = Student('Leonid', 'Mamontov', 'Male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grade_st(best_lecturer, 'Python', 9)
best_student.grade_st(lecturer, 'Pediatrician', 3)

student = Student('Sofia', 'Bohan', 'Female')
student.courses_in_progress += ['Rehabilitation science', 'Pediatrician']
student.finished_courses += ['Exercise therapy']
student.grade_st(best_lecturer, 'Python', 2)
student.grade_st(lecturer, 'Exercise therapy', 10)

best_reviewer = Reviewer('Alena', 'Batitskaia')
best_reviewer.courses_attached += 'Git', 'Java', 'HTML'
best_reviewer.rate_hw(best_student, 'Git', 9)
best_reviewer.rate_hw(best_student, 'Java', 8)
best_reviewer.rate_hw(best_student, 'HTML', 9)

reviewer = Reviewer('Nadya', 'Bohan')
reviewer.courses_attached += 'mathematics', 'story', 'literature'
reviewer.rate_hw(student, 'Mathematics', 10)
reviewer.rate_hw(student, 'Story', 8)
reviewer.rate_hw(student, 'Literature', 7)


students = [best_student, student]
lecturers = [best_lecturer, lecturer]

def average_student_course(students, course):
    average_grade = []
    for student in students:
        if course in student.grades:
            average_grade += student.grades[course]
    if average_grade:
        return sum(average_grade) / len(average_grade)

# Функция подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lectors_course(lecturers, course):
    average_grade = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            average_grade += lecturer.grades[course]
    if average_grade:
        return sum(average_grade) / len(average_grade)

print(best_student)
print(student)
print(best_lecturer)
print(lecturer)
print(best_reviewer)
print(reviewer)



