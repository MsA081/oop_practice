class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Student(Person):
    def __init__(self, name, age, address, id_student, email):
        super().__init__(name, age, address)
        self.id_student = id_student
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    def display_info(self):
        return f"""students_details:\n
                   name : {self.name}\n
                   age : {self.age}\n
                   address : {self.address}\n
                   id_student : {self.id_student}\n
                   email : {self.email}"""


class Teacher(Person):
    def __init__(self, name, age, address, id_teacher, subject):
        super().__init__(name, age, address)
        self.id_teacher = id_teacher
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        self._subject = new_subject

    def display_info(self):
        return f"""teacher_details:\n
                   name : {self.name}\n
                   age : {self.age}\n
                   address : {self.address}\n
                   id_teacher : {self.id_teacher}\n
                   subject : {self.subject}"""


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self._students = []
        self._teacher = teacher

    @property
    def students(self):
        return self._students

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        self._teacher = teacher

    def display_info(self):
        return f"""course_details:\n
                   name : {self.name}\n
                   teacher : {self.teacher.name}\n
                   students : {[student.name for student in self.students]}"""


# تست کردن پیاده‌سازی
s1 = Student('Ali', 23, "Tehran", 1, "ali@gmail.com")
s2 = Student('Sara', 22, "Shiraz", 2, "sara@gmail.com")
s3 = Student('Reza', 24, "Mashhad", 3, "reza@gmail.com")
s4 = Student('Neda', 21, "Isfahan", 4, "neda@gmail.com")

t1 = Teacher('Mr. Smith', 40, "New York", 101, "Mathematics")
t2 = Teacher('Mrs. Johnson', 35, "Los Angeles", 102, "Physics")

c1 = Course("Math 101", t1)
c2 = Course("Physics 101", t2)

# اضافه کردن دانشجو به دوره‌ها
c1.add_student(s1)
c1.add_student(s2)
c2.add_student(s3)
c2.add_student(s4)

# نمایش اطلاعات دوره‌ها
print(c1.display_info())
print(c2.display_info())

# به‌روزرسانی ایمیل یکی از دانشجویان
s1.email = "ali_new@gmail.com"
print(s1.email)

# حذف دانشجو از یک دوره
c1.remove_student(s1)
print(c1.display_info())

# اضافه کردن دانشجوی بیشتر به دوره‌ها
c1.add_student(s3)
c2.add_student(s1)

print(c1.display_info())
print(c2.display_info())
