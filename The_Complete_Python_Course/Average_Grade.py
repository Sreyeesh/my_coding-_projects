my_student =  {
    'name': 'Harry Potter',
    'grades': [70,88,90,99]
    
}

def student_name():
    return my_student['name']

print('this is the student name',student_name())

def student_grade():
    return my_student['grades']

print('these are the student grades',student_grade())

#get the average of the student grade printed with name and average grade. 

def average_grade(student):
    total = 0

    for grade in student():
        total = total + grade
        avg_wizard = total/ len(student)

print(average_grade(my_stud))

