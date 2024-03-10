# Import statements
import json
import employee as emp
def create_dict():
    """ Creates a dictionary that stores an employee's information

    1. Return a dictionary that maps "first_name" to name, "age" to age, and "title" to title

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments, respectively. Make sure that 
               the values are typecasted correctly (name - string, age - int, 
               title - string)
    
    WRITE YOUR SOLUTION BELOW
    """
    emp.dict = {
      "first_name" :str(emp.employee_name),
      "age" : int(emp.age),
      "title":str(emp.title )
      }
    print(emp.details())
    return emp.dict

create_dict()

json_object = json.dumps(emp.dict)

def write_json_to_file():
    """ Write json string to file

    1. Open a new file defined by output_file
    2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
     
    WRITE YOUR SOLUTION BELOW
    """
    new_file = open("output_file","w")
    new_file.write(json_object)
    new_file.close
        
print(write_json_to_file())        
        

def main():
    # Print the contents of details() -- This should print the details of an employee
    

    # Create employee dictionary
   

    # Use a function called dumps from the json module to convert employee_dict
    # into a json string and store it in a variable called json_object.
    

    # Write out the json object to file
    

 if __name__ == "__main__":
    main()
