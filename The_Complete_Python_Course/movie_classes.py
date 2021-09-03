# Define a Movie class that has two properties: name and director
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director
 
# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')