# sample code

# Writing to a file
with open ("sample.txt","w") as file:
    file.write("Hello World!\n")
    file.write("This is a Sample File\n")
    
# Reading From a File 
with open ("sample.txt","r") as file:
    contents = file.read()
    print("File Contents: ",contents)   
    
# Storing File Content in a List
with open ("sample.txt","r") as file:
    lines = file.readlines()
    print("File Contents as List: ",lines)

# 1. Write a program that reads a text file (data.txt) line by line and prints each line.

with open ("data.txt","w") as file:
    file.write("x+y = 17 \n")
    file.write("Hello World! \n")
    file.write("The New Generation of Ai & ML \n")
    file.write("Black Box AI \n")

# # Reading line by line
def read_line_print_file(file_path):
    with open(file_path,"r") as file:
        for line in file:
            print(line.strip())  # strip() function removes unwanted characters from a string

file_path = 'data.txt'
read_line_print_file(file_path)

# 2. Modify the sample code to append additional text to the existing file instead of 
# overwriting it.
def append_text_to_file(file_path,text_to_append):
    with open (file_path,'a') as file:
        file.write(text_to_append)
        
file_path = 'sample.txt'
text_to_append = "Black Box the Most Powerful Ai with the option of \n (You  can create your own AI Assistant) for a specific Task"

append_text_to_file(file_path,text_to_append) 

def read_line_from_file(file_path):
    print("Reading after appending: ")
    with open(file_path,"r") as file:
        for line in file:
          print(line.strip())      
      
file_path = 'sample.txt'
read_line_from_file(file_path)