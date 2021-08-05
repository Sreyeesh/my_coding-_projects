movies = []
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f',' to find a movie by title, 'find_movie_director command for  movie director ,'find_release_year' command for find year released or 'q' to quit: "



# You may want to create a function for this code

def add_to_movie_database():
    movie_title = input("Enter the movie title: ")
    movie_director = input("Enter the movie director: ")
    movie_year = input("Enter the movie release year: ")
    movies.append(

        {
            'movie_title': movie_title,
            'movie_director': movie_director,
            'movie_year': movie_year
        }
    )


#list movies

def list_movies():
    for movie in movies:
        print_movie(movie)

#print movies



def print_movie(movie):
    print(f"Title: {movie['movie_title']}")
    print(f"Director: {movie['movie_director']}")
    print(f"Release year: {movie['movie_year']}")
    print()

#find movies

def find_movies():
     user_search = input("what movies would you like to find ? ")
     for movie in movies:
         if movie['movie_title'] == user_search:
             print(movie['movie_title'])

#find director

def find_movie_director():
     user_search = input("what movie director would you like to find ? ")
     for movie in movies:
         if movie['movie_director'] == user_search:
             print(movie['movie_director'])





def find_year_released():
     user_search = input("what release date would you like to find ? ")
     for movie in movies:
         if movie['movie_year'] == user_search:
             print(movie['movie_year'])



menu_selection = {
    "a": add_to_movie_database,
    "l": list_movies,
    "f": find_movies,
    "fyrd": find_year_released,
    "fmd": find_movie_director

}


# And another function here for the user menu



def menu():
    # walrus operator - DRY


    
    while (user_selection := input(MENU_PROMPT)) != 'q':
        for selection in menu_selection:
            if user_selection == selection:
                menu_selection[selection]()  # list_movies()


menu()


