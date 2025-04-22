class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def get_all_students(self):
        return self.student_list

    def find_student_by_id(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None
class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.name = name
        self.student_id = student_id
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if self.is_enrolled:
            print(f"Student {self.student_id} is already enrolled.")
            return False
        else:
            self.is_enrolled = True
            print(f"Student {self.student_id} has been enrolled.")
            return True

    def drop_student(self):
        if not self.is_enrolled:
            print(f"Student {self.student_id} is not currently enrolled.")
        else:
            self.is_enrolled = False
            print(f"Student {self.student_id} has been dropped.")

    def view_student_info(self):
        stat = "Enrolled" if self.is_enrolled else "Not Enrolled"
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Status: {stat}\n")
def sclin():
    db = StudentDatabase()
    db.add_student(Student("S101", "Alice Smith", "Computer Science", True))
    db.add_student(Student("S102", "Bob Johnson", "Electrical Engineering"))
    db.add_student(Student("S103", "Carol White", "Mechanical Engineering", True))
    while True:
        print("\n===== Student Management Menu =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        check = input("Enter your choice (1-4): ")

        if check == '1':
            all_students = db.get_all_students()
            if not all_students:
                print("No students in the database.")
            else:
                for student in all_students:
                    student.view_student_info()

        elif check == '2':
            student_id = input("Enter student ID to enroll: ")
            student = db.find_student_by_id(student_id)
            if student:
                student.enroll_student()
            else:
                print("Error: Student ID not found.")

        elif check == '3':
            student_id = input("Enter student ID to drop: ")
            student = db.find_student_by_id(student_id)
            if student:
                student.drop_student()
            else:
                print("Error: Student ID not found.")

        elif check == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
sclin()
