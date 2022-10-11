# Robert Savoie
# Sept 22/2022
# Python file
# Allows a user to decide how many movies to add to the list then
# determines the average budget and displays information on all entered movies

movies = [("Eternal Sunshine of the Spotless Mind", 20000000),
          ("Memento", 9000000),
          ("Requiem for a Dream", 4500000),
          ("Pirates of the Caribbean: On Stranger Tides", 379000000),
          ("Avengers: Age of Ultron", 365000000),
          ("Avengers: Endgame", 356000000),
          ("Incredibles 2", 200000000)]

# Ask the user how many movies they wish to add
x = int(input("Enter how many movies you wish to add: "))

# Run a for loop for the range of movies the user wants to add
# request user input for movie name and budget
# Create movie tuple with user input
# Append tuple to list
for y in range(x):
    movie_name = input("\nEnter new movie name: ")
    movie_budget = int(input("Enter movie budget: "))
    movie = (movie_name, movie_budget)
    movies.append(movie)

# Declare total_budget
# Then for each movie in movies add the movie budget to total_budget
total_budget = 0
for movie in movies:
    total_budget += movie[1]

# Calculate average budget using the length of the movies list
# Convert average_budget to int to remove trailing .0
average_budget = total_budget / len(movies)
average_budget = int(average_budget)

print("\nAverage Budget: ", round(average_budget, 0), "\n")

# Create a counter
# For each movie in movies if movie budget is above the average budget
# increment counter, subtract the average budget from budget, and then
# print the information
counter = 0
for movie in movies:
    if movie[1] > average_budget:
        counter += 1
        over_budget = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]} : ${over_budget} over average.")

print(f"\nThere were {counter} movies with an above average budget.")
