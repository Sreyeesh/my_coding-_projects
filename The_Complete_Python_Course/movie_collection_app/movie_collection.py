from dataclasses import dataclass
 
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f',' to find a movie by title, 'fd' to find movie director ,'fyr' to find year released or 'q' to quit: "
movies = []
 
@dataclass
class Movie:
   movie_title: str
   movie_director: str
   release_year: str
 
   def __str__(self):
       return """Title: {movie_title}
        Director: {movie_director}
        Release year: {release_year}""".format(movie_title=self.movie_title, movie_director=self.movie_director, release_year=self.release_year)


# Prompts user to add a movie to the movies database.
#
# @param movie Adds movie to database.
def add_to_movie_database(movie):
   movies.append(movie)
 
# List movie by title 
#
# @param title The title to search for.
# @return Movie if found. Else returns None
def list_movie_by_title(movie_title: str):
   for movie in movies:
       if movie.movie_title == movie_title:
           return movie
   return None

#find movie by title
def find_movie_by_title(movie_title: str):
       for movie in movies:
        if movie.movie_title == movie_title:
           return movie
        return None
# Searches for a movie by director.
#
# @param director The director to search for.
# @return Movie if found. Else returns None.
def find_movie_by_director(movie_director):
   for movie in movies:
       if movie.movie_director == movie_director:
           return movie
   return None

# @param year The year to search for.
# @return Movie if found. Else returns None.
def find_movie_by_year(release_year):
   for movie in movies:
       if movie.release_year == release_year:
           return movie
   return None

def menu_selection():
    selection = input(MENU_PROMPT)
    while selection != 'q':
       if selection == "a":
           movie_title = input("Enter the movie title: ")
           movie_director = input("Enter the movie director: ")
           release_year = input("Enter the movie release year: ")
           add_to_movie_database(Movie(movie_title, movie_director, release_year))
           print("Added movie with title {}!".format(movie_title))
       
       elif selection == "l":
            for movie in movie_title:
                print('these are movies added',movie_title)
                movie = list_movie_by_title(movie_title)
                if (movie is not None):
                    print(movie)
                else:
                 print("Movie with title \"{}\" not found!".format(movie_title))
       
       elif selection =="f":
            movie_title = input("find movie title:")
            for movie in movie_title:
                print(movie)
                movie = find_movie_by_title(movie_title)
                if(movie is not None):
                    print(movie)
                else:
                    print("Movie with title \"{}\" not found!".format(movie_title))
       
       elif selection == "fd":
           movie_director = input("Search movie by director:")
           movie = find_movie_by_director(movie_director)
           print(movie)
           if (movie is not None):
               print(movie)
           else:
               print("Movie with director \"{}\" not found!".format(movie_director))

       elif selection == "fyr":
           release_year = input("Search movie by year:")
           movie = find_movie_by_year(release_year)
           print(movie)
           if (movie is not None):
               print(movie)
           else:
               print("Movie with selection \"{}\" not found!".format(selection))
       else:
           print('Unknown command. Please try again.')
       selection = input(MENU_PROMPT)

menu_selection()