 
wizard_students = {
     'name': 'Harry Potter',
    'grades':[70,75,60,50],
    'average': None  #Something Here
    
}


def student_name():
    return wizard_students['name']

print('this is the student name',student_name())

#get the average of the student grade printed with name, list , and average grade.
#test
def getAverageGrade(grades):
    """Return the average grades

    args:
        grades ([int])

    returns:
        float
    """

    return sum(grades) / len(grades)

print("Average grade: {}".format(getAverageGrade(wizard_students.get('grades'))))

class Student:
    #class contains functions #  
    #self is a blank object, that was created before we called dunder init function
    def __init__(self,new_name,new_grade): #this is a dunder init function
        self.name = new_name
        self.grade = new_grade

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student_one =  Student('Hermione Granger', [100,90,89,100]) 

# this creates new object of type student
#Object is something that can store data, and we tell it what data to store

student_two = Student('Ron Weasley', [80,75,70,60])

print(student_one.name,student_one.grade)
print(student_two.name,student_two.grade)
