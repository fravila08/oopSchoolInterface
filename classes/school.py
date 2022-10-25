# school.py
from classes.staff import Staff
from classes.students import Student


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.open_staff_csv()
        self.students = Student.opening_csv()
        
    def list_all_students(self):
        for student in Student.students:
            print(student)
            
    def grab_stud_by_id(self):
        id=input("input student id: \n")
        for student in Student.students:
            if student.school_id== id:
                print(student)
                
    def add_a_student(self):
        run=True
        while(run):
            new_stud={}
            new_stud['name']=input("Name:\n")
            new_stud['age']=input("age: \n")
            new_stud['role']= input("role: \n")
            new_stud['password']=input("password: \n")
            wanting_id=input("Desired Id: \n")
            confirm=Student.no_repeated_id(wanting_id)
            if confirm == False:
                print("id already exist")
            else:
                print("good id")
                new_stud['school_id']=wanting_id
                run=False
        Student.students.append(Student(**new_stud))
        print("student was added")
        
    def remove_a_student(self):
        id=input("what is the id: \n")
        for student in Student.students:
            if student.school_id == id:
                Student.students.remove(student)
        print("a student was removed")
        
    def list_staff(self):
        for i in Staff.staff:
            print(i)
        