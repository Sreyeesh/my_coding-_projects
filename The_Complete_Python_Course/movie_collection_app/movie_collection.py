# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_to_movie_database():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
    'title': title,
    'director': director,
    'year': year
})

add_to_movie_database()

# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
def menu_selection():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            pass
        elif selection == "l":
            pass
        elif selection == "f":
            pass
        else:
            print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)