class Movie:
    def __init__(self,name,year):
        self.name = name  # name is a property of self and is not a variable  the variable is getting created inside of self
        self.year = year #

Jurassic_Park = Movie('Jurassic Park', 1993)

print(Jurassic_Park.name)