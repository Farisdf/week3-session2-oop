import json
 
 
# ==================== PART 1 - Person and Student ====================
 
class Person:
    """A person in the university. This is the parent class."""
 
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
 
    def describe(self):
        """Print a simple description of the person."""
        print("Person " + str(self.person_id) + ": " + self.name)
 
 
# Student IS-A Person, because every student is also a person: a student
# has an id and a name just like any person, and only adds a major on top.
# Inheritance makes sense here because we reuse the Person data and
# behaviour instead of writing it again inside Student.
class Student(Person):
    """A student. Inherits everything from Person and adds a major."""
 
    def __init__(self, person_id, name, major):
        # super() calls the parent __init__ so Person sets up id and name
        super().__init__(person_id, name)
        self.major = major
 
    # method overriding: Student has its own version of describe()
    def describe(self):
        """Print a description that also shows the major."""
        print("Student " + str(self.person_id) + ": " + self.name
              + " - major: " + self.major)
 
    # ==================== PART 2 - Special Method ====================
 
    def __str__(self):
        """Return text shown when we print a Student object."""
        # must RETURN a string, not print it
        return ("Student(id=" + str(self.person_id) + ", name=" + self.name
                + ", major=" + self.major + ")")
 
 
# ==================== PART 3 - Course ====================
 
class Course:
    """One university course."""
 
    def __init__(self, code, name, seats):
        self.code = code
        self.name = name
        self.seats = seats
 
    def __str__(self):
        return (self.code + " - " + self.name
                + " (" + str(self.seats) + " seats)")
 
 
# ============ PART 4 and 5 - Enrollment, grade property, composition ============
 
# Enrollment HAS-A Student and HAS-A Course. An enrollment is not a kind of
# student and not a kind of course, so inheritance would be wrong here.
# It simply connects two existing objects together plus a grade, which is
# exactly what composition means.
class Enrollment:
    """Connects one Student, one Course, and one grade."""
 
    def __init__(self, student, course, grade):
        self.student = student      # a real Student object, not a string
        self.course = course        # a real Course object, not a string
 
        # using the property below, so the grade given here is validated too
        self.grade = grade
 
    @property
    def grade(self):
        """Give back the private grade."""
        return self.__grade
 
    @grade.setter
    def grade(self, value):
        """Only allow a grade between 0 and 100."""
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100, but got "
                             + str(value))
        self.__grade = value        # the two underscores make it private
 
    def __str__(self):
        return (self.student.name + " -> " + self.course.code
                + " : grade " + str(self.grade))
 
 
# ==================== PART 6 - Registry ====================
 
class Registry:
    """Owns all the students, courses and enrollments of the system."""
 
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []
 
    def add_student(self, student):
        self.students.append(student)
 
    def add_course(self, course):
        self.courses.append(course)
 
    def enroll_student(self, student, course, grade):
        """Create an Enrollment object and keep it in the list."""
        enrollment = Enrollment(student, course, grade)
        self.enrollments.append(enrollment)
        return enrollment
 
    def show_students(self):
        print("--- Students ---")
        for student in self.students:
            print(student)
 
    def show_courses(self):
        print("--- Courses ---")
        for course in self.courses:
            print(course)
 
    def show_enrollments(self):
        print("--- Enrollments ---")
        for enrollment in self.enrollments:
            print(enrollment)
 
 
# ==================== PART 8 - Build the system ====================
 
registry = Registry()
 
# three students
student1 = Student(101, "Lina", "Computer Science")
student2 = Student(102, "Omar", "Information Systems")
student3 = Student(103, "Sara", "Software Engineering")
 
registry.add_student(student1)
registry.add_student(student2)
registry.add_student(student3)
 
# two courses
course1 = Course("CS101", "Introduction to Programming", 2)
course2 = Course("DB101", "Introduction to Databases", 3)
 
registry.add_course(course1)
registry.add_course(course2)
 
# three enrollments
registry.enroll_student(student1, course1, 85)
registry.enroll_student(student2, course1, 90)
registry.enroll_student(student3, course2, 78)
 
 
# ---------- Part 1 test: describe() on both classes ----------
print("===== Part 1: describe() =====")
person = Person(100, "Ahmad")
person.describe()
student1.describe()
print()
 
# ---------- Part 2 test: printing a Student ----------
print("===== Part 2: print a Student =====")
print(student1)
print()
 
# ---------- Part 3 test: printing Courses ----------
print("===== Part 3: Courses =====")
print(course1)
print(course2)
print()
 
# ---------- Part 4 test: the grade property ----------
print("===== Part 4: grade property =====")
enrollment = registry.enrollments[0]
print("grade is:", enrollment.grade)
 
try:
    enrollment.grade = 150          # this must be rejected
except ValueError as error:
    print("Rejected:", error)
print()
 
# ---------- Part 5 test: composition ----------
print("===== Part 5: composition =====")
print(enrollment.student.name)      # reach the Student through Enrollment
print(enrollment.course.code)       # reach the Course through Enrollment
print(enrollment.grade)
print()
 
# ---------- Part 8 test: show everything ----------
print("===== Part 8: the whole system =====")
registry.show_students()
print()
registry.show_courses()
print()
registry.show_enrollments()
print()
 
 
# ==================== PART 7 - Error handling ====================
 
print("===== Part 7: enter a grade =====")
try:
    typed = input("Enter a grade for Lina in CS101 (0-100): ")
 
    # int() raises ValueError if the text is not a number, like "hello"
    number = int(typed)
 
    # the Enrollment property raises ValueError if it is outside 0-100
    new_enrollment = registry.enroll_student(student1, course2, number)
 
    print("Enrollment created:", new_enrollment)
 
except ValueError as error:
    # one except catches BOTH problems, because both raise ValueError
    print("Sorry, that grade was not accepted.")
    print("Reason:", error)
print()
 
 
# ==================== PART 9 - Save students to JSON ====================
 
print("===== Part 9: save to students.json =====")
 
# json cannot save objects directly, so we build a list of dictionaries
students_data = []
for student in registry.students:
    students_data.append({
        "person_id": student.person_id,
        "name": student.name,
        "major": student.major
    })
 
with open("students.json", "w") as file:
    json.dump(students_data, file, indent=4)
 
print("students.json was created.")
print()
