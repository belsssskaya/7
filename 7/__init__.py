#родительский класс
class Human:
 #инициализация атрибутов класса
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
#получение имени
    def get_name(self):
        return self.name
#измнение возраста
    def change_gender(self, new_gender):
        self.gender = new_gender

#дочерний класс
class Student(Human):
    def __init__(self, name, age, gender, university, faculty, course):
        super().__init__(name, age, gender)
        self.university = university
        self.faculty = faculty
        self.course = course
#получаем всю информацию
    def get_info(self):
        return f"Student: {self.name}, {self.age} years old, studying at {self.university}, {self.faculty}, {self.course} course."
#дочерний класс
class Teacher(Human):
    def __init__(self, name, age, gender, university, faculty, subjects):
        super().__init__(name, age, gender)
        self.university = university
        self.faculty = faculty
        self.subjects = subjects
#получение информации
    def get_info(self):
        return f"Teacher: {self.name}, {self.age} years old, working at {self.university}, {self.faculty}, teaching {', '.join(self.subjects)}."
#дочерний класс
class DepartmentChair(Human):
    def __init__(self, name, age, gender, university, faculty, teachers):
        super().__init__(name, age, gender)
        self.university = university
        self.faculty = faculty
        self.teachers = teachers
#получение информации
    def get_info(self):
        return f"Department Chair: {self.name}, {self.age} years old, working at {self.university}, {self.faculty}."
#вводим информацию о человеке
def add_person(people):
    print("Adding a new person:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    role = input("Enter role (student/teacher/department chair): ")
#родолжаем вводить в зависимости от роли
    if role == "student":
        university = input("Enter university: ")
        faculty = input("Enter faculty: ")
        course = int(input("Enter course: "))
        person = Student(name, age, gender, university, faculty, course)

    elif role == "teacher":
        university = input("Enter university: ")
        faculty = input("Enter faculty: ")
        subjects = input("Enter subjects (comma-separated): ").split(", ")
        person = Teacher(name, age, gender, university, faculty, subjects)

    elif role == "department chair":
        university = input("Enter university: ")
        faculty = input("Enter faculty: ")
        person = DepartmentChair(name, age, gender, university, faculty, [])

    else:
        print("Invalid role!")
        return

    people.append(person)
    print("Person added successfully!\n")

#функция вывода всех людей
def show_people(people):
    print("People in the registry:")
    for person in people:
        print(person.get_info())
    print()


def main():
    people = []
    while True:
        print("==== Console Registry ====")
        print("1. Add person")
        print("2. Show all people")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_person(people)
        elif choice == "2":
            show_people(people)
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()