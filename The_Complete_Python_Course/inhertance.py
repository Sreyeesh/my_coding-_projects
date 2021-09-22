"""
use inheratince to reduce duplication 


"""
class Student:
    def __init__(self, name,school):
        self.name = name
        self.school =school
        self.marks =[]

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student): #working student is a child of student 
    def __init__(self, name,school,salary):
        super().__init__(name,school)  # It's a parent class
        self.salary = salary 

    def weekly_salary(self):
        return self.salary * 37.5


    # def average(self):
    #     return sum(self.marks) / len(self.marks)

rolf = WorkingStudent('Rolf','MIT',15.50)        

print(rolf.salary)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
print(rolf.weekly_salary())


