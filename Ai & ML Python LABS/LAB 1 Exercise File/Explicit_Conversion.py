# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

name = "Alice"
age = 20
height = 5.70
loyalty = True
name = str(name)
age = int(age)
height = float(height)
loyalty = bool(loyalty)

print(f"name: {name} (type{type(name)})")
print(f"age: {age} (type{type(age)})")
print(f"height: {height} (type:{type(height)})")
print(f"loyalty: {loyalty} (type:{type(loyalty)})")