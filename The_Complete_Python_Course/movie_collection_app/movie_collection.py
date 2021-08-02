# Incomplete app!
 
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f',' to find a movie by title, 'fd' to find movie director ,'fyd' to find year released or 'q' to quit: "
movies = []
 
 
# You may want to create a function for this code
def add_to_movie_database():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
 
    movies.append(
        {
            'title': title,
            'director': director,
            'year': year
        }
    )
# menu_selection = {
#     "a": add_to_movie_database,
# }

#list movies
def list_movies():
    user_search = input("What movie would you like to list ? ")
 
    for movie in movies:
        if movie['title'] == user_search:
            print_movie(movie)

#print movies

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

print_movie(movie)

#find movies
def find_movies():
     user_search = input("what movies would you like to find ? ")

     for movie in movies: 
         if movie['title'] == user_search:
             print(movie['title'])


# menu_selection = {
#     "a": add_to_movie_database,
#     "l": list_movies,
#     "f": find_movies(),
    
# }
find_movies()


#find director 
def find_director():
     user_search = input("what movies would you like to find ? ")

     for movie in movies: 
         if movie['director'] == user_search:
             print(movie['director'])


# menu_selection = {
#     "a": add_to_movie_database,
#     "l": list_movies,
#     "f": find_movies(),
#     "fd": find_director()
# }
  

find_director()

def find_year_released():
     user_search = input("what release date would you like to find ? ")

     for movie in movies: 
         if movie['year'] == user_search:
             print(movie['year'])


# menu_selection = {
#     "a": add_to_movie_database,
#     "l": list_movies,
#     "f": find_movies(),
#     "fd": find_year_released()
# }
  

find_year_released()



# And another function here for the user menu

def menu_selection():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_to_movie_database()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movies()
        elif selection == "fd":
            find_director()
        elif selection == "fyr":
            find_year_released()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)
 
 
menu_selection()