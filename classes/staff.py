from classes.persons import Person
import csv


class Staff(Person):
    staff=[]
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['password'])
        self.employee_id = kwargs['employee_id']
    
    def __str__(self):
        return f"{self.name}, {self.role}"
    @classmethod   
    def open_staff_csv(self):
        with open('./data/staff.csv', newline='') as staff:
            reader = csv.DictReader(staff)
            for row in reader:
                self.staff.append(Staff(**row))