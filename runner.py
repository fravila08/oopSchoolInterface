from classes.school import School

school = School('Ridgemont High') 

run=True
while(run):
    choice=input("""What would you like to do?
Options:
1. List All Students
2. View Individual Student <student_id>
3. Add a Student
4. Remove a Student <student_id>
5. Quit
""")
    if choice=="1":
        school.list_all_students()
    elif choice=="2":
        school.grab_stud_by_id()
    elif choice=="3":
        school.add_a_student()
    elif choice=="4":
        school.remove_a_student()
    elif choice=="5":
        run=False
    elif choice=='6':
        school.list_staff()
    else:
        print("incorrect input")