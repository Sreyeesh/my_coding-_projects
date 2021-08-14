my_student =  {
    'name': 'Harry Potter',
    'grades': [70, 88, 90, 99],
    #'average':#something here
}

# don't really need a function for this, I would just use the built in dictionary 'get'
# my_student.get("name") or what you have below, the wrapper is just extra steps and only good
# for the one variable.

def student_name():
    return my_student['name']

print('this is the student name',student_name())

#get the average of the student grade printed with name, list , and average grade.

def getAverageGrade(grades):
    """Return the average grades
    args:
        grades ([int])
    returns:
        float
    """

    return sum(grades) / len(grades)

print("Average grade: {}".format(getAverageGrade(my_student.get('grades'))))