x = 10

def my_function():
    y = 20
    print("Inside Function",x,y)

my_function()
print("Outside Function",x)
    
# Write a Python program that demonstrates variable scope. Define a 
# global variable global_var and a function called test_scope that defines a local variable 
# local_var. Inside the function, print both global_var and local_var. Outside the function, 
# print only global_var. 

global_var = 5

def test_scope():
    local_var = 7
    print("Inside Function",global_var,local_var)
    
test_scope()
print("Outside Function",global_var)    