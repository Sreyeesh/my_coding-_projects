# class Student: 
#   def __init__(self,name):
#     self.name = name

# movies = ['Matrix', 'Finding Nemo']
# print(movies.__class__)

# #everything in python is an object 
# print(len(movies))

class Garage:
  def __init__(self) -> None:
      self.cars = []
  def __len__(self):
      return len(self.cars)
  def __getitem__(self,i):
      return self.cars[i]
  def __repr__(self) -> str: # repr method gets used when you are coding for debugging
      return f'<Garage {self.cars}>'

  def __str__(self):
      return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

# for car in ford: 
#    print(car)

print(ford)


# print(len(ford)) # this tells you how many cars there inside your garage . 

# class Garage: 
#    def __init__(self,car_make_one,car_make_two) -> None:
#       self.car_make_one = []
#       self. car_make_two = []

#       car_make_one = 'Fiesta'
#       car_make_two = 'Focus'



    