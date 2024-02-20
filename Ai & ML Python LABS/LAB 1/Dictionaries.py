student = {'name': "Alice",'Age':20,'grade':"A"}
print(student)
print(student['name'])
student['Age'] = 21
print(student)
student['city'] = "New York"
print(student)
student.pop('grade')
print(student)

# Write a Python program that creates a dictionary containing the names of 
# your friends as keys and their corresponding ages as values. Then, print the age of a specific 
# friend. 

Friend_Dictionary = {"Shah": 22,"Umar": 20,"Ahmed": 21,"Tayyab": 23}
print(Friend_Dictionary)
print("Age = ",Friend_Dictionary["Shah"])
print("Age = ",Friend_Dictionary["Ahmed"])
