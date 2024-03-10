# Modify the sample code to include a custom exception called CustomError. Raise this 
# exception when the user enters a negative number.

# Sample Code
class CustomError(Exception):
    pass 
try:
    x = int (input("Enter a Number: "))
    if x<0:
        raise CustomError("Negative Numbers are not allowed!")
    y = int (input("Enter a Number: "))
    if y<0:
        raise CustomError("Negative Numbers are not allowed!")
    y = 10/x
    print("y =",y)
except ValueError:
    print("Invalid! Please Enter a Valid Integer.")
except ZeroDivisionError:
    print("Cannot be Divided by Zero")        
except CustomError as e:
    print(e)  
except Exception as e:
    print("An Error occured, e") 
    
    

    