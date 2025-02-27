students = []

def choices():
    while (1):
        print("Select the choice:")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Update Student")
        print("3. Delete Student")
        print("4. Exit")

        opt = int(input("Select an option: "))
        match opt:
            case 1: add_student()
            case 2: show_students()
            case 3: update_student()  
            case 3: delete_student()
            case 4: exit()

def add_student():
    student_id = int(input("Enter the student id: "))
    student_name = input("Enter the student name: ")
    student_rollno = int(input("Enter the student roll number: "))
    
    student = [student_id, student_name, student_rollno]
    students.append(student)
    print("Student added successfully")

def show_students():

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Roll No: {student[2]}")

def update_student():
    student_id = int(input("Enter the student id to update: "))
    for student in students:
        if student[0] == student_id:
            student_name = input("Enter the student name: ")
            student_rollno = int(input("Enter the student roll number: "))
                                 
            print("Student updated successfully")        

def delete_student():
    show_students()
    student_id = int(input("Enter the student id to delete: "))
    for student in students:
        if student[0] == student_id:
            students.remove(student)
            print("Student deleted successfully")

choices()
