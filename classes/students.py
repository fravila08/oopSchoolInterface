from classes.persons import Person
import csv
import os

class Student(Person):
    students=[]
    def __init__(self, name, age, role, school_id, password):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id
        
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, role: {self.role}, password: {self.password}"
    
    @classmethod
    def opening_csv(self):
        with open('./data/students.csv', newline='') as students:
            reader = csv.DictReader(students)
            for row in reader:
                self.students.append(Student(**row))
            
    @classmethod
    def no_repeated_id(self, want):
        for student in self.students:
            if student.school_id == want:
                return False
        return True
