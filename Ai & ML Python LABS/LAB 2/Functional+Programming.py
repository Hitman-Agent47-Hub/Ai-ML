# # simple Function
def add(a,b):
    return a+b

print("sum = ",(add(5,7)))

# # Recursive Function
def factorial(n):
    if n== 0:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial = ",factorial(5))    

# map() Function to double each number in a list

numbers = [1,2,3,4,5]
doubled_numbers = list(map(lambda x: x*2,numbers))
print ("Doubled Numbers: ",doubled_numbers)

# filter() Function to filter even numbers from a list

even_numbers = list(filter(lambda x: x%2 == 0,numbers))
print("Even Numbers: ",even_numbers)

# List comprehensions to generate squares of numbers
squares = [x** 2 for x in numbers]
print("Squares: ",squares)
