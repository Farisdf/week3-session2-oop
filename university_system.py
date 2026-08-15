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
