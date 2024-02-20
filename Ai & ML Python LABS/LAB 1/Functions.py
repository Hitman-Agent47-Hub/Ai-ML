def greet(name):
    """_summary_
     Greets the user with the given name.
    Args:
        name (_type_): _description_
    """
    return "Hello " + name + "!"
print(greet("Alice"))

# Write a Python function called calculate_area that takes the length and 
# width of a rectangle as parameters and returns its area.

def calculate_Area(length, width):
    """Compute Area of Rectangle """
    return length*width
print("Area of Rectangle = ",calculate_Area(5, 3)) 
