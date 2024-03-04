# Modify the line below
# name = input('What is your name? ')

# print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

name = str(input('What is Your Name? '))
try: 
    type(name) == str
    print(f"Type of variable name is correct: {type(name)}")
except:
    print(f"Type of variable name is incorrect: {type(name)}.It should be <class 'str'>")

# Modify the line below
# age = input('What is your age? ')

# print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# age = input('What is your age? : ')
# age = int(str(age))
# if type(age) == int:
#     print(f"Type of age variable is correct: {type(age)}")
# else:
#     print(f"Type of age variable is incorrect: {type(age)}.It should be <class 'int'>")