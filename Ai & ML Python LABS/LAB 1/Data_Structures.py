# Lists  Mutable (changable)

fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[1])
fruits[2] = "mango"
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.insert(2,"pineapple")
print(fruits)
fruits.remove("kiwi")
print(fruits)

# # Write a Python program that creates a list of your favorite movies, then 
# # adds a new movie to the list and prints the updated list

Favourite_movies = ["John Wick","Hitman","Transformers"]
print(Favourite_movies)
Favourite_movies.append("Star Wars")
print(Favourite_movies)
Favourite_movies.insert(2,"The Matrix")
print(Favourite_movies)

# Tuples Immutable (Unchangeable)

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_week)
print(days_of_week[0])

# Write a Python program that creates a tuple containing the names of the 
# months, then prints the months in reverse order.

Months = ("January","February","March","April","May","June","July","August","September","October","November","December")
print(Months)
print(Months[::-1])