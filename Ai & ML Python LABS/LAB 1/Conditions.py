x = 10
if x>0:
    print("X is Positive")
else:
    print("X is Negative")
    
y = -5
if(y>0):
    print("Y is Positive")
elif y == 0:
    print("Y is zero")
else:
    print("Y is Negative")
        
# Write a Python program that takes an integer as input from the user and 
# prints whether it is positive, negative, or zero. 

z = float(input("Enter a Number: "))
if z>0:
    print("z is Positive")
elif z<0:
    print("z is Negative")
else:
    print("z is Zero Neither positive nor Negative")
    
# Write a Python program that takes a grade (A, B, C, D, or F) as input 
# from the user and prints a corresponding message (e.g., "Excellent", "Good", "Average", 
# "Pass", "Fail").

grade = str(input("Enter a Grade: ")) # Grades from A to F
if grade == "A" or grade == "a":
    print ("Excellent")
elif grade == "B" or grade == "b":
    print ("Good")
elif grade == "C" or grade == "c":
    print ("Average")
elif grade == "D" or grade == "d":
    print ("Pass")   
else:
    print ("Fail")         