def greet (**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
        
        
greet(name="Alice", age="30") 
    
# Write a Python function called calculate_sum that takes an arbitrary 
# number of keyword arguments representing numbers and returns their sum

def calculate_sum(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
        print(key,":",value)
    print("sum=",sum)

print(calculate_sum(n=1,n1=2,n3=3,n4=4,n5=5))
    
  