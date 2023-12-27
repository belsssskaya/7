class Human:
    def __init__(self):
        return


    def get_name(self):
        return

    def change_gender(self, new_gender):
        pass

class Student(Human):
    def __init__(self, name, age, gender, university, faculty, course):
       pass

    def get_info(self):
        return

class Teacher(Human):
    def __init__(self, name, age, gender, university, faculty, subjects):
        return

    def get_info(self):
        return

class DepartmentChair(Human):
    def __init__(self, name, age, gender, university, faculty, teachers):
        return

    def get_info(self):
        return

def add_person(people):
    print("Adding a new person:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    role = input("Enter role (student/teacher/department chair): ")

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


def show_people(people):
    print("People in the registry:")
    return