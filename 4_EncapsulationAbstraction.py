# Encapsulation is a method of hiding data implementation.
# Instance attributes or variables are kept private.
# There is only one accessor method from outside with which we can access or change these instance variables.
# Same can be done with methods , instance methods can be kept private.....
# So private means can be accessed only internally.....

class Employees:
    # Class attributes.
    all_employees_hike = 0.5
    
    # Instance attributes.
    def __init__(self,position,name,age,phone_number,email_id): # email_id - mandatory, no_children =0 non mandotory instance because we can give a default.
        self.position = position
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self._salary = None 
        self.email_id = email_id 
        self._no_children = None # private _ use single underscore, # real private __ use double underscore..
        # Techically we use _ and is conidered private it should not be accessed outside but still accessible in python.
        # __ is not seen much used but _ is used.
        # Correct conentions for access modifiers in Python:
        # public variables: Example: self.name, etc.
        # _x : protected attribute
        #__x private attribute.
        # But _x is also considered private.

    # private instance method - used only inside the class.
    def child_support_incrementer(self):
        self._no_children += 1
    
    # Why we use getter and setter?
    # getter
    def get_salary(self):
        return self._salary
    
    # setter
    # check value, have conditions i.e enforce some constraints,
    #def set_salary(self,value):
        if value < 1000:
            self._salary = 1000 
        elif value >35000:
            self._salary = 35000 
        else:
            self._salary =value
    def set_salary(self,base_salary,no_of_children):
        self._salary = self._calculate_child_support_compensation(base_salary,no_of_children)
    
    
    # Calculate compensation based on the number of children.
    def _calculate_child_support_compensation(self,base_value,value):
        self._no_children = value
        if self._no_children > 3:
            return base_value * 2
        else:
            return base_value * 1.5

    # Instance method. - public
    def work(self):
        print(f"{self.name} is working.")
    # Instance method.  - public
    def access_email(self): 
        user_name = self.name
        password = self.email_id
        print(f"{user_name} is going to login to the server with the credentials {password}.")
    # Instance method.  - public
    def order_food(self,hotel):
        print(f"{self.name} is ordering food from {hotel}. The service will be done as soon as possible")
    # Instance method.   - public
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

# 'extend' functionality under Inheritance.
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
data_scientist_1 = DataScience('data scientist','Ashwin',26,111111111,"ashwin@employee.com") # Creating an instance or an object.
Web_developer_1 = WebDevelopment('web developer','Arjun',26,111111131,"arjun@employee.com") # Creating an instance or an object.
ios_developer_1 = IosDevelopement('ios developer','Arin',26,111111141,"arin@employee.com") # Creating an instance or an object.
android_developer_1 = AndroidDevelopement('android developer','Awain',26,111111161,"awain@employee.com") # Creating an instance or an object.
blackberry_developer_1 = BlackberryDevelopement('blackberry developer','Allul',26,111111151,"allul@employee.com") # Creating an instance or an object.
# Biology
pharmacologist_1 = Pharma('drug scientist','Ashwin',26,111111171,"ashwin12@employee.com") # Creating an instance or an object.
mcb_1 = MCB('mcb','Adi',26,111111191,"adi@employee.com") # Creating an instance or an object.
radiologist_1 = Radiology('radiologist','Arjun',26,111111181,"ashwin@employee.com") # Creating an instance or an object.

print("Understanding Encapsulation")
# Understanding Encapsulation.
print(data_scientist_1._no_children)
print(data_scientist_1._salary)

print(" ")
# When we have just functions to get and set.
data_scientist_1.set_salary(77000000,2)
print(data_scientist_1.get_salary())
print(data_scientist_1._salary) # Still not restricted but accessible.

# Abstraction can be thought as a natural extension to Encapsulation.
# Should use high level mechanism which hides internal details.
# It should only reveal relevant information of the objects and hide sensitive information and restrict actions on sensitive attributes and functions......
# set_salary() is an example of abstraction.....



