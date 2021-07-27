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


#   - listing movies
def list_movies():
    for m in  movie_title:
        user_search = input("What movie are you looking for ? ")
        print(user_search,m)
       
list_movies()


 



