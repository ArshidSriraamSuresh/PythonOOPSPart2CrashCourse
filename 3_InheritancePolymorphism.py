# Inheritance
# Inheritance is the process by which one class inherits the attributes and methods of another class.
# The newly formed class is the child class. The class from which everything was inherited is known as parent class.
# Parent class also known as base class......
class Employees:
    # Class attributes.
    all_employees_hike = 0.5
    
    # Instance attributes.
    def __init__(self,position,name,age,phone_number,salary,email_id,no_children =0): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        self.position = position
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        self.email_id = email_id
        self.no_children = no_children
    # Instance method.
    def work(self):
        print(f"{self.name} is working.")
    # Instance method.
    def access_email(self):
        user_name = self.name
        password = self.email_id
        print(f"{user_name} is going to login to the server with the credentials {password}.")
    # Instance method.
    def order_food(self,hotel):
        print(f"{self.name} is ordering food from {hotel}. The service will be done as soon as possible")
    # Instance method.
    def employee_info(self):
        # you dont need to write a seperate information instance method because we have pre-built special methods __str__ and __repr__ for this purpose.
        employee_info = f"name: {self.name}, age: {self.age}, phone number employee: {self.phone_number}, email id employee: {self.email_id}, position in the organisation: {self.position}"
        return employee_info

    # Special methods in Python.
    def __str__(self):
        employee_info = f"name: {self.name}, age: {self.age}, phone number employee: {self.phone_number}, email id employee: {self.email_id}, position in the organisation: {self.position}"
        return employee_info
    # Special methods in Python.
    def __eq__(self,other):
        return self.name == other.name and self.email_id == other.email_id and self.phone_number == other.phone_number
    
    # Static methods in Python.
    @staticmethod
    def calculate_entry_salary(age):
        if age<23:
            return 10000
        elif age<45:
            return 15000
        else:
            return 18000




employee_1 = Employees('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com") # Creating an instance or an object.
employee_2 = Employees('biologist','Sriram',16,111111111,2500,"sriram@employee.com") # Creating an instance or an object.

# Here in these two objects employee_1 and employee_2 though thery are both employees they work in different fields.
# For example employee_1 works in 'Data Science but employee_2 works in "Science".
# It is wise to have a scheme of classification of employees.
# Example:
# Parent class: Employees
# Child class: Based on position like Computer Science, Biology,HR, Admin etc.

# Inheritance - Examples Child class will inherit from the parent class.
# For employee 1
# Define Child class - Computer Science
class ComputerScience(Employees):
    pass
# Define Child class of Computer Science.
class DataScience(ComputerScience):
    pass
# Define Child class of Computer Science.
class WebDevelopment(ComputerScience):
    pass
# Define Child class of Computer Science.
class IosDevelopement(ComputerScience):
    pass
# Define Child class of Computer Science.
class AndroidDevelopement(ComputerScience):
    pass
# Define Child class of Computer Science.
class BlackberryDevelopement(ComputerScience):
    pass

# For employee 2
# Define Child class - Biology
class Biology(Employees):
    pass
# Define Child class of Biology.
class Pharma(Biology):
    pass
# Define Child class of Biology.
class MCB(Biology):
    pass
# Define Child class of Biology.
class Radiology(Biology):
    pass

# Creating Objects
# Computer Science 
data_scientist_1 = DataScience('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com") # Creating an instance or an object.
Web_developer_1 = WebDevelopment('web developer','Arjun',26,111111131,2000,"arjun@employee.com") # Creating an instance or an object.
ios_developer_1 = IosDevelopement('ios developer','Arin',26,111111141,2000,"arin@employee.com") # Creating an instance or an object.
android_developer_1 = AndroidDevelopement('android developer','Awain',26,111111161,2000,"awain@employee.com") # Creating an instance or an object.
balckberry_developer_1 = BlackberryDevelopement('blackberry developer','Allul',26,111111151,2000,"allul@employee.com") # Creating an instance or an object.

# Biology
pharmacologist_1 = Pharma('drug scientist','Ashwin',26,111111171,2000,"ashwin12@employee.com") # Creating an instance or an object.
mcb_1 = MCB('mcb','Adi',26,111111191,2000,"adi@employee.com") # Creating an instance or an object.
radiologist_1 = Radiology('radiologist','Arjun',26,111111181,2000,"ashwin@employee.com") # Creating an instance or an object.

print("Understanding Inheritance")
# Understanding Inheritance.
data_scientist_1.work()
print(data_scientist_1.all_employees_hike)

android_developer_1.work()
print(android_developer_1.all_employees_hike)

radiologist_1.work()
print(radiologist_1.all_employees_hike)

print(" ")


# 'extend' functionality under Inheritance.
# Define Child class - Computer Science
class ComputerScience(Employees):
    def __init__(self,position,name,age,phone_number,salary,email_id,main_programming_language,coding_speed,no_children =0): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        super().__init__(position,name,age,phone_number,salary,email_id,no_children)
        self.main_programming_language = main_programming_language
        self.coding_speed = coding_speed

    # Unique instance method for Computer Science class.....
    def code(self):
        print(f"{self.name} is coding in {self.main_programming_language}.")


# Define Child class of Computer Science.
class DataScience(ComputerScience):
    def __init__(self,position,name,age,phone_number,salary,email_id,main_programming_language,coding_speed,cloud_expert_level,no_children =0): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        super().__init__(position,name,age,phone_number,salary,email_id,no_children,main_programming_language,coding_speed)
        self.cloud_expert_level = cloud_expert_level

    # Unique instance method for Computer Science class.....
    def cloud_level(self):
        print(f"{self.name} knows the cloud technology as a {self.cloud_expert_level}.")

print("Understanding 'extend' functionality under Inheritance.")
print("The instance methods created in respective child classes are unique only to the child class and is not applicable to parent class or any other child class.....")

# Understanding 'extend'.
data_scientist_1 = DataScience('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com","Java","professional","pro") # Creating an instance or an object.
data_scientist_1.work()
print(data_scientist_1.all_employees_hike)
data_scientist_1.cloud_level()


print(" ")

# 'Override' functionality under Inheritance.
# When you use the __init__ constructor again in child class we are using overwriting principle under inheritance and that is why we use super().__init() to call the parent class instance attributes.
# Note: If you dont overwrite the __init__ constructor in child class we still have access to __iniT__ constructor in parent class.....
# We can overwrite any instance method defined in parent class.
class ComputerScience(Employees):
    def __init__(self,position,name,age,phone_number,salary,email_id,main_programming_language,coding_speed,no_children =0): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        super().__init__(position,name,age,phone_number,salary,email_id,no_children)
        self.main_programming_language = main_programming_language
        self.coding_speed = coding_speed

    # Unique instance method for Computer Science class.....
    def code(self):
        print(f"{self.name} is coding in {self.main_programming_language}.")
    # already present function in parent class Employees
    def order_food(self):
        print(f"{self.name} is ordering food but the choice is always Italian.")

# Define Child class of Computer Science.
class DataScience(ComputerScience):
    def __init__(self,position,name,age,phone_number,salary,email_id,main_programming_language,coding_speed,cloud_expert_level,no_children =0): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        super().__init__(position,name,age,phone_number,salary,email_id,no_children,main_programming_language,coding_speed)
        self.cloud_expert_level = cloud_expert_level

    # Unique instance method for Computer Science class.....
    def cloud_level(self):
        print(f"{self.name} knows the cloud technology as a {self.cloud_expert_level}.")
    # already present function in parent class ComputerScience.....
    def order_food(self):
        print(f"{self.name} is ordering food but the choice is always Chineese.")

print("Understanding 'Override' functionality under Inheritance.")
# Understanding 'Override'.
data_scientist_1 = DataScience('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com","Java","professional","pro") # Creating an instance or an object.
data_scientist_1.work()
print(data_scientist_1.all_employees_hike)
data_scientist_1.cloud_level()
data_scientist_1.order_food() # See this output the last overwriting has worked. That is see DataScience class.



print(" ")

# Polymorphism
# Polymorphism and inheritance are related and works hand in hand.
class Radiology(Biology):
    def work(self):
        print(f"This function is overwritten.....")
employee_all = [
    DataScience('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com","Python","pro","pro"),
    WebDevelopment('web developer','Arjun',26,111111131,2000,"arjun@employee.com"),
    IosDevelopement('ios developer','Arin',26,111111141,2000,"arin@employee.com"),
    AndroidDevelopement('android developer','Awain',26,111111161,2000,"awain@employee.com"),
    BlackberryDevelopement('blackberry developer','Allul',26,111111151,2000,"allul@employee.com"),
    Pharma('drug scientist','Ashwin',26,111111171,2000,"ashwin12@employee.com"),
    MCB('mcb','Adi',26,111111191,2000,"adi@employee.com"),
    Radiology('radiologist','Arjun',26,111111181,2000,"ashwin@employee.com") 
]

print("Polymorphism explained.")
print("The work functioned in parent class employees took many forms based on different child classes, example work is redefined in radiology.")
# Polymorphism in action defined through a function.....
def employee_all_work(employee_all):
    for employee in employee_all:
        employee.work()

employee_all_work(employee_all)


# Conclusion or recap:
# Inheritance: ChildClass(BaseClass)
# Inherit attributes and functions.
# Extend attributes and functions.
# Override attributes and functions.

# super().__init__() if we override the __init__() in Child class we sould call super().__init__() of base class.
# Also we learned about polymorphism.

