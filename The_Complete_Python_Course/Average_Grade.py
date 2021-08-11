my_student =  {
    'name': 'Harry Potter',
    'grades': [70,88,90,99]
    
}

def student_name():
    return(my_student['name'])

print('this is the student name',student_name())

def student_grade():
    return(my_student['grades'])

print('these are the student grades',student_grade())

#get the average of the student grade printed with name, list , and average grade. 

def average_grade(student):
    sum = 0

    for g in student:
        sum = sum + g
        # print(sum)

        avg_wizard = sum /len(student)
        return avg_wizard
    

print('This is the average of the wizarding student',average_grade(my_student['grades']))
   

