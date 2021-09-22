my_student = {
    'name': 'Rolf Smith',
    'grades': [ 70,88,90,99],
    'average': None #something here
}

class Student:
  def __init__(self, new_name, new_grades):
    self.name = new_name
    self.grades = new_grades

  def average(self):
    return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Sreyeesh', [50, 60, 99, 100])

# print(student_one.name,student_one.grades)
# print(student_two.name,student_two.grades)


print(student_one.average())
print(student_two.average())

#in methods first parameter is called self 



























