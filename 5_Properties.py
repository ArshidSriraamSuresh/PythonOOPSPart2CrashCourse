# Instead og get_salary() and set_salary() there is more Pythonic way of doing this.

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
        self._no_children = None 
        


    
    # Why we use getter and setter?
    # getter
    @property
    # We can have internal constraints as well here.
    def salary(self): # Use the method without protection, don't use _salary.
        return self._salary
    
    # setter
    # check value, have conditions i.e enforce some constraints,
    @salary.setter
    def salary(self,value):
        self._salary = value
    
    @salary.deleter
    def salary(self):
        del self._salary
    
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

print("Understanding Properties - Getter and Setter.")
# Understanding Encapsulation.
print(" ")
# When we have just functions to get and set.
data_scientist_1.salary = 77000
print(data_scientist_1.salary)
#del data_scientist_1.salary
print(data_scientist_1.salary)

# Recap
# Encapsulation principle.
# Abstraction principle.
# public and private methods and attributes.
# Example: private function: _function_name() , _attribute_name / _variable_name.
# Normal way: getter and setter.
# Pythonic way: Getter and setter instead of get and set function.
# Getter ---> @property
# Setter ---> @function_name.setter


# OOPS Priciples recap:
# Reference/Attribution: https://www.youtube.com/watch?v=-pEs-Bss8Wc
# See OOPS principles recap where definitions are given.


