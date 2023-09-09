import matplotlib.pyplot as plt
import os

# Function to clear the terminal screen
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

# Class representing a Student
class Student:
    # Constructor to initialize student properties
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.registered_courses = []
        self.schedule = {}
        self.course_scores = {} 

    # Method to schedule a course for the student
    def schedule_course(self, course, time):
        if course.name in self.schedule:
            print(f"Course '{course.name}' is already scheduled for student '{self.name}' at time '{self.schedule[course.name]}'.")
        else:
            self.schedule[course.name] = time
            print(f"Course '{course.name}' scheduled for student '{self.name}' successfully!")

    # Method to display student details
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("Registered Courses:")
        for course in self.registered_courses:
            print(f"{course.name}")
        ave = self.average()
        print(f"AVG: {ave:.2f}")

    # Method to register for a course
    def registerCourse(self, course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)
            course.addStudent(self)

    # Method to withdraw from a course
    def withdrawCourse(self, course):
        if course in self.registered_courses:
            self.registered_courses.remove(course)
            course.removeStudent(self)

    # Method to add a score for a course
    def addScore(self, course, score):
        self.course_scores[course.name] = score

    # Method to calculate the average score
    def average(self):
        if not self.course_scores:
            return 0

        total_score = sum(self.course_scores.values())
        ave = total_score / len(self.course_scores)
        return ave

    def schedule_course(self, course, time):
        self.schedule[course.name] = time

# Class representing a Course
class Course:
    # Constructor to initialize course properties
    def __init__(self, name, course_code, credits):
        self.name = name
        self.course_code = course_code
        self.credits = credits
        self.registered_students = []

    # Method to display course details
    def showDetails(self):
        print(f"Course Name: {self.name}")
        print(f"Course Code: {self.course_code}")
        print(f"Credits: {self.credits}")
        print("Registered Students:")
        for student in self.registered_students:
            print(f"{student.name}")

    # Method to add a student to the course
    def addStudent(self, student):
        if student not in self.registered_students:
            self.registered_students.append(student)

    # Method to remove a student from the course
    def removeStudent(self, student):
        if student in self.registered_students:
            self.registered_students.remove(student)

# Class representing a Student Management System
class StudentManagementSystem:
    # Constructor to initialize the system with empty student and course lists
    def __init__(self):
        self.students = []
        self.courses = []

    # Method to create a new student and add it to the student list
    def createStudent(self, name, student_id, major):
        student = Student(name, student_id, major)
        self.students.append(student)
        return student

    # Method to create a new course and add it to the course list
    def createCourse(self, name, course_code, credits):
        course = Course(name, course_code, credits)
        self.courses.append(course)
        return course

    # Method to manage registration or withdrawal of a student from a course
    def manage_registration(self, student, course, action):
        if student in self.students and course in self.courses:
            if action == "register":
                student.registerCourse(course)
            elif action == "withdraw":
                student.withdrawCourse(course)
            else:
                print("Invalid action. Use 'register' or 'withdraw'.")
        else:
            print("Student or course not found in the system.")

    # Method to search for students based on a keyword
    def search_students(self, keyword):
        results = []
        for student in self.students:
            if keyword in student.name or keyword == student.student_id:
                results.append(student)
        return results

    # Method to generate a report of students and their course scores
    def generate_student_report(self):
        for student in self.students:
            student.showDetails()
            print("Course Scores:")
            for course_name, score in student.course_scores.items():
                print(f"{course_name}: {score}")

    # Method to generate a report of courses and their enrollment status
    def generate_course_report(self):
        for course in self.courses:
            course.showDetails()


# Main program execution
if __name__ == "__main__":
    sms = StudentManagementSystem()

    while True:
        # Display the main menu
        print("\nWelcome to the Student Management System!")
        print("1. Create a new student")
        print("2. Create a new course")
        print("3. Register a student for a course")
        print("4. Withdraw a student from a course")
        print("5. Schedule a course for a student")
        print("6. Search for a student")
        print("7. Generate student report")
        print("8. Generate course report")
        print("9. add student scores")
        # Quit the program
        print("10. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")
        clear_screen()

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            major = input("Enter student major: ")
            existing_student = next((student for student in sms.students if student.student_id == student_id), None)
            if existing_student:
                print(f"Student with ID '{student_id}' already exists as '{existing_student.name}'!")
            else:
                student = sms.createStudent(name, student_id, major)
                print(f"Student '{student.name}' created successfully!")
                

        elif choice == "2":
            name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            credits = int(input("Enter course credits: "))
            existing_course = next((course for course in sms.courses if course.course_code == course_code), None)
            if existing_course:
                print(f"Course with code '{course_code}' already exists as '{existing_course.name}'!")
            else:
                course = sms.createCourse(name, course_code, credits)
                print(f"Course '{course.name}' created successfully!")


        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            student = None
            course = None
            for s in sms.students:
                if s.student_id == student_id:
                    student = s
                    break
            for c in sms.courses:
                if c.course_code == course_code:
                    course = c
                    break
            if student and course:
                sms.manage_registration(student, course, "register")
                print(f"Student '{student.name}' registered for course '{course.name}' successfully!")
            else:
                print("Student or course not found in the system.")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            student = None
            course = None
            for s in sms.students:
                if s.student_id == student_id:
                    student = s
                    break
            for c in sms.courses:
                if c.course_code == course_code:
                    course = c
                    break
            if student and course:
                sms.manage_registration(student, course, "withdraw")
                print(f"Student '{student.name}' withdrew from course '{course.name}' successfully!")
            else:
                print("Student or course not found in the system.")

        elif choice == "5":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            time = input("Enter course schedule time: ")
            student = None
            course = None
            for s in sms.students:
                if s.student_id == student_id:
                    student = s
                    break
            for c in sms.courses:
                if c.course_code == course_code:
                    course = c
                    break
            if student and course:
                sms.manage_registration(student, course, "schedule")
                print(f"Course '{course.name}' scheduled for student '{student.name}' successfully!")
            else:
                print("Student or course not found in the system.")
        elif choice == "6":
            keyword = input("Enter a keyword to search for a student: ")
            results = sms.search_students(keyword)
            if results:
                print("Search results:")
                for i, student in enumerate(results, 1):
                    print(f"{i}. {student.name} (Student ID: {student.student_id})")
            else:
                print("No students found matching the keyword.")

        elif choice == "7":
            sms.generate_student_report()

        elif choice == "8":
            sms.generate_course_report()

        elif choice == "9":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            score = float(input("Enter the score for the course: "))
            student = None
            course = None
            for s in sms.students:
                if s.student_id == student_id:
                    student = s
                    break
            for c in sms.courses:
                if c.course_code == course_code:
                    course = c
                    break
            if student and course:
                student.addScore(course, score)
                print(f"Score {score} assigned for course '{course.name}' for student '{student.name}' successfully!")
            else:
                print("Student or course not found in the system.")

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7/8/9).")


students = sms.students
student_names = [student.name for student in students]
student_averages = [student.average() for student in students]

courses = sms.courses
course_names = [course.name for course in courses]
course_enrollment = [len(course.registered_students) for course in courses]

plt.figure(figsize=(10, 6))
plt.bar(student_names, student_averages)
plt.xlabel('Students')
plt.ylabel('Average Score')
plt.title('Student Academic Progress')
plt.xticks(rotation=45)
plt.tight_layout()

plt.figure(figsize=(10, 6))
plt.bar(course_names, course_enrollment)
plt.xlabel('Courses')
plt.ylabel('Enrollment')
plt.title('Course Enrollment Status')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plots
plt.show()
