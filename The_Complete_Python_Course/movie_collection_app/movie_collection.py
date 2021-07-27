# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

movie_title = ['title']
movie_director = ['director']
movie_year = ['year']

# You may want to create a function for this code
def add_to_movie_database():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({ # adding to the empty list of movies 
    'title': title,
    'director': director,
    'year': year
})

add_to_movie_database()

# Create other functions for:

#   - listing movies
def list_movies():
    for m in  movie_title:
        user_search = input("What movie are you looking for ? ")
        if m in movie_title == user_search:
           print('this is the movie title you are looking for',m)
        print('list of movies',m)

list_movies()

#   - finding movies
def find_movies(): 
   user_search = input("What movie are you looking for ? ")

   for m in movies:
       if m in movie_title == user_search:
           print('this is the movie title you are looking for',m)
        
find_movies()

#find director 
def find_director():
    user_search = input('What movie director are you looking for ? ')
    for d in movie_director:
        if d in movie_director == user_search:
            print('this is the movie director you are looking for: ',d)

find_director()

#find year released 
def year_released():
    user_search = input("What is the release year of  the movie you are looking for ? ")
    for ry in movie_year:
        print('this are  the movies  year the movie released in this year',movie_year)

year_released()

# And another function here for the user menu

def menu_selection():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
           return add_to_movie_database()
        elif selection == "l":
           return list_movies()

        elif selection == "f":
            return find_movies()
        
        elif selection == "f":
            return find_director()

        else:
            print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)