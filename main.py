class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        text = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценки за домашнее задание: {self.__calc_average()}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )
        return text

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__calc_average() < other.__calc_average()
        else:
            return

    def __calc_average(self):
        if len(sum(self.grades.values(), [])) != 0:
            return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        else:
            return 0

    def rate_lectures(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        text = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценки за лекции: {self.__calc_average()}\n"
            f"Ведет курсы: {', '.join(self.courses_attached)}"
        )
        return text

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__calc_average() < other.__calc_average()
        else:
            return

    def __calc_average(self):
        if len(sum(self.grades.values(), [])) != 0:
            return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        else:
            return 0

    def rate_hw(self):
        return 'Лектор не может оценивать студенов'


class Reviewer(Mentor):
    def __str__(self):
        text = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )
        return text


# Не очень понятно, зачем две разные функции для студентов и лекторов. Структура одинаковая же
def average_student_or_lecture(students_or_lectures, course_name):
    average_grades = 0
    count_of_grades = 0
    for student_or_lecture in students_or_lectures:
        for course, grades in student_or_lecture.grades.items():
            if course == course_name:
                average_grades += sum(grades)
                count_of_grades += len(grades)
    if count_of_grades != 0:
        return average_grades / count_of_grades
    else:
        return 0


rev_kuzin = Reviewer("Алексей", "Кузин")
rev_kuzin.courses_attached += ["Математика", "Физика"]
rev_matveev = Reviewer("Семен", "Матвеев")
rev_matveev.courses_attached += ["Химия", "История"]

student_petrov = Student("Александр", "Петров", "мужчина")
student_petrov.courses_in_progress += ["Математика", "Физика"]
student_petrov.finished_courses += ["История", "Химия"]

student_alexandrova = Student("Анастасия", "Александрова", "женщина")
student_alexandrova.courses_in_progress += ["Математика", "Физика", "Химия"]
student_alexandrova.finished_courses += ["История"]

lector_ivanov = Lecturer("Сергей", "Иванов")
lector_ivanov.courses_attached += ["Физика", "Химия"]

lector_sima4kov = Lecturer("Вячеслав", "Симачков")
lector_sima4kov.courses_attached += ["История"]

rev_kuzin.rate_hw(student_petrov, "Математика", 4)
rev_kuzin.rate_hw(student_petrov, "Математика", 5)
rev_kuzin.rate_hw(student_alexandrova, "Математика", 3)

rev_matveev.rate_hw(student_alexandrova, "Химия", 4)

student_petrov.rate_lectures(lector_ivanov, "Физика", 4)
student_petrov.rate_lectures(lector_sima4kov, "История", 3)

student_alexandrova.rate_lectures(lector_ivanov, "Физика", 3)
student_alexandrova.rate_lectures(lector_sima4kov, "История", 4)
student_alexandrova.rate_lectures(lector_ivanov, "Химия", 5)

print()
print("СТУДЕНТЫ:")
print(student_petrov)
print("------------")
print(student_alexandrova)

print()
print("ЛЕКТОРЫ")
print(lector_ivanov)
print("------------")
print(lector_sima4kov)

print()
print("ПРОВЕРЯЮЩИЕ:")
print(rev_kuzin)
print("------------")
print(rev_matveev)

print()
print(f"Средняя оценка по студентам: {average_student_or_lecture([student_petrov, student_alexandrova], 'Математика')}")
print(f"Средняя оценка по лекторам: {average_student_or_lecture([lector_ivanov, lector_sima4kov], 'Физика')}")

print()
if lector_ivanov < lector_sima4kov:
    print("Лучший лектор - Симачков")
else:
    print("Лучший лектор - Иваное")

print()
if student_petrov > student_alexandrova:
    print("Лучший студент - Петров")
else:
    print("Лучший студент - Александрова")
