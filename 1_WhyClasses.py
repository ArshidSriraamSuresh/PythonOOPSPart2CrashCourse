# 1a. Create Classes - Why, How.
# 1b. Class vs instance in Python.
# 2. Functions inside classes.
# 3. Inheritance (Base class + Child class)
# 4. Encapsulation (Private/Public)
# 5. Properties (Getter/Setter)

# The four principles of OOPS

#1. Inheritance.
#2. Polymorphism.
#3. Encapsulation.
#4. Abstraction.

# 1a. Why we need classes?
# primitive data types in Python cant represent complex logic.....
# We need classes to create a blue print or design for our own complex data structure.

# Let us create an employee
# Attributes or properties of employee: position, name, age, phone number, salary, email id

# Lets use primitive data type.
employee_1 = ['data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com"]
employee_2 = ['biologist','Sriram',16,111111111,2500,"sriram@employee.com"]
print(employee_1)
print(employee_2)
print(type(employee_1))
# When we create more of these lists it can get dirty,error prone and cumbersome.
# So we need something a blueprint that could manipulate these dynamic information - general charecteristics  like  position, name, age, phone number, salary, email id which are common for all the employees.

# Example what if we miss some value like position or salary and so on.
# We need to set rules and a proper blueprint.........

# Now we cannot relate the list to the functions or actions that particular data scientist does or biologists does.
# So list is not a perfect data structure for representing complex objects and these are the reasons for a class.

# Classes are used for more complex data structures in Python.
# Classes contains functions which describe the behaviour of the object or class or static functions that does not alter the behaviour of an object or class.
# classes are blueprint of how something should be defined.

# How we create class in Python.
# Keyword 'class'.

# By convention we use Pascal case for class names in Python......

# Step 1: Creating a class.
# This is a valid class in Python.
class Employees:
    # Class attributes.
    all_employees_hike = 0.5
    # A class attribute is applicable to entire class and all the instance s created from it.

    # Instance attributes each time has unique outside parameters so dynamically changed with every instance.
    # Instance attributes.....
    # Create instance attributes.
    # Instance attributes:  position, name, age, phone_number, salary, email_id 
    # We can define the instance attributes in __init__ constructor.
    # 'self' is the first argument because it is where the instance itself is passed.
    # Outside parameters are position, name, age, phone_number, salary, email_id which are stored inside the class as a part of the instance.
    # That particular instance is denoted by 'self'.
    def __init__(self,position,name,age,phone_number,salary,email_id):
        self.position = position
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        self.email_id = email_id

#1b. Class vs instance in Python.
# So a class is a blue print of how the data structure looks.
# We dont put any concrete information in a class other than class attributes.
# We can write properties or attributes, actions or methods in a class.........

# Instance or object creation.
# Step 2: Creating an instance of the class also known as a object after creation.
employee_1 = Employees('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com") # Creating instance
print(employee_1.position) # Acessing instance attribute.
print(employee_1.email_id) # Acessing instance attribute.
print(employee_1.age) # Acessing instance attribute.
print(employee_1.phone_number) # Acessing instance attribute.
print(employee_1.salary) # Acessing instance attribute.
print(employee_1.email_id) # Acessing instance attribute.
print(type(employee_1)) # Acessing instance attribute.


# An instance access the created class or bluperint with real time data or concrete information and objects are created from the class.........

# This is not possible
#print(Employees.name) # NameError: name 'Employees' is not defined
# Because name is an instance attribute applicable to only instances or objects created from class.

print(Employees.all_employees_hike) # Accessing class attribute with the class itself.
# This is possible because it is a class attribute.
# Class attributes can be accessed from instance as well.
print(employee_1.all_employees_hike) # Acessing class attribute with the created instance.

# Conclusion - Class attributes vs instance attributes:
# 1. Instance attributes are tied to a particular instance or a object and is not applicable or cannot be accessed from a class.
# 2. Class attributes is applicable to entire class and all instances or objects created can access it.........


# Create employee_2
employee_2 = Employees('biologist','Sriram',16,111111111,2500,"sriram@employee.com") # Creating instance
print(employee_2.position) # Acessing instance attribute.
print(employee_2.email_id) # Acessing instance attribute.
print(employee_2.age) # Acessing instance attribute.
print(employee_2.phone_number) # Acessing instance attribute.
print(employee_2.salary) # Acessing instance attribute.
print(employee_2.email_id) # Acessing instance attribute.
print(employee_2.all_employees_hike) # Acessing class attribute with the created instance.
print(type(employee_2))


# Final Conclusion:
# 1. Creating a class - Class is a blueprint for objects or instances.
# 2. Create an instance - Concrete data or instance attributes are dynamically assigned for each instance.
# 3. Instance are also called as objects.
# 4. Instance attributes are defined in __init__(self).
# 5. Class attribute - Class attribute is applicable to whole class and all instances created.
# 6. Instance attributes are dynamically assigned in __init__(self) for each instance.

