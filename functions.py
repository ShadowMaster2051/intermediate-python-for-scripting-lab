import math

def validate_age(age):
    '''
    This function validates age as an integer.
    
    Simply pass an integer this function and it will check 
    to ensure it's a positive number and not a decimal
    
    If a decimal or a negative number is passed, it will raise
     a ValueError Exception
     '''
    
    # check if age in an integer 
        # if not integer, raise error 
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")

    # check if age integer is positive
        #if not positive, raise error
    if age <=0:
        raise ValueError("Age must be a greater than zero")
    return age 

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def get_area(shape, *args):
    # make sure shape is rectangle or circle 
        # normalize the input
    shape = shape.lower().strip()
    # validate input 
    if shape not in ["reactangle", "circle"]:
        raise ValueError("Shape must be rectangle or circle")
    if shape == "rectangle":
    # if it's rectangle, extract l &w from args
        # tuple unpacking 
        length, width = args 
        # then pass values to calculate rect area
        return calculate_rectangle_area(length, width)
    else:
    #otherwise extract radius from args
        #then pass radius to calculate circle area 
        #assign a radius variable to the first index of args
        # use index positioning to extract radius
        radis = args[0]
        return calculate_circle_area(radius)  
    
#print(get_area("circle", 50))
print(get_area("rectangle" ,10, 5))