colors = {"red", "green", "blue","black"}
print(colors)
colors.add("yellow")
colors.add("white")
print(colors)
colors.remove("green")
# print(colors)

# Write a Python program that takes a list of numbers as input from the 
# user and creates a set containing only the unique numbers from the list.

Numbers = int(input("Enter a list of numbers: "))
set = set(Numbers)
print(set)
