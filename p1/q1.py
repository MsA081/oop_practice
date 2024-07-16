class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Student(Person):
    def __init__(self, student_id, email, name, age, address):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.email = email

    @property
    def change_email(self):
        return self.email

    @change_email.setter
    def change_email(self, new_email):
        self.email = new_email

    def display_info(self):
        print(f"Student ID: {self.student_id}\t"
              f"student_email: {self.email}\t"
              f"name: {self.name}\t"
              f"age: {self.age}\t"
              f"address: {self.address}")


class Teacher(Person):
    def __init__(self, teacher_id, subject, name, age, address):
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject

    @property
    def change_subject(self):
        return self.subject

    @change_subject.setter
    def change_subject(self, new_subject):
        self.subject = new_subject

    def display_info(self):
        print(f"Student ID: {self.teacher_id}"
              f"student_email: {self.subject}"
              f"name: {self.name}"
              f"age: {self.age}"
              f"address: {self.address}")


class Course:
    def __init__(self, course_name, students, teacher):
        self.course_name = course_name
        self.students = list(students)
        self.teacher = teacher

    def add_student(self, student_name):
        self.students.append(student_name)
        return self.students

    def remove_student(self, student_name):
        for student in self.students:
            if student == student_name:
                self.students.remove(student_name)
                return True

    @property
    def teacher(self):
        return self.teacher

    @teacher.setter
    def teacher(self, teacher):
        self.teacher = teacher

    def display_info(self):
        print(f"Course: {self.course_name}"
              f"students: {self.students}"
              f"teacher: {self.teacher}")
