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
    # What are instance methods:
    # 1. Instance methods accept the instance itself as 'self' as the first argument or parameter.
    # 2. Instance methods modify the behaviour of particular instance.
    # 3. 'self' parameter refers to the instance itself.........
    # 4. With 'self' we can access object or instance specific attributes like self.position,self.name,self.age,self.phone_number,self.salary,self.email_id.
    def access_email(self):
        user_name = self.name
        password = self.email_id
        print(f"{self.name} is going to login to the server.")
    # We can pass other parameters to the instance method.
    def order_food(self,hotel):
        print(f"{self.name} is ordering food from {hotel}. The service will be done as soon as possible")
    # We can return from instance methods using return statement.
    def employee_info(self):
        # you dont need to write a seperate information instance method because we have pre-built special methods __str__ and __repr__ for this purpose.
        employee_info = f"name: {self.name}, age: {self.age}, phone number employee: {self.phone_number}, email id employee: {self.email_id}, position in the organisation: {self.position}"
        return employee_info
    # Special methods in Python.
    # Special methods 0r __methods like __init__ constructor.
    # Special methods are pre built and are already provided to us by Python.
    # Also known as dunder methods.........
    # Special method __str__
    # Should return 
    # It is used to return the object info as a string.
    def __str__(self):
        employee_info = f"name: {self.name}, age: {self.age}, phone number employee: {self.phone_number}, email id employee: {self.email_id}, position in the organisation: {self.position}"
        return employee_info
    
    # This special method __eq__ is used to compare two objects.
    # By default without __eq__ it compares the memory address..........
    # But with __eq__ it compares the parameters we mention.
    # Returns True or False.
    def __eq__(self,other):
        return self.name == other.name and self.email_id == other.email_id and self.phone_number == other.phone_number
    
    # Static methods in Python.
    # Static methods are not tied to an instance.
    # Static methods neither receives self or cls as an argument.
    # @staticmethod decoraor is used.
    # Can be accessed by class as well as the instance.
    # But we cannot use the instance attributes inside the static method because we are not passing the instance as an argument as 'self'.........
    @staticmethod
    def calculate_entry_salary(age):
        if age<23:
            return 10000
        elif age<45:
            return 15000
        else:
            return 18000




employee_1 = Employees('data scientist','Ashwin',26,111111111,2000,"ashwin@employee.com") # Creating an instance or an object.
# Note: We dont need to pass self because it is automatically passed as self in the instance method.
# Each instance itself is passed as self.
employee_1.access_email()
employee_1.order_food('KFC')
info_1 = employee_1.employee_info()
print(info_1)

employee_2 = Employees('biologist','Sriram',16,111111111,2500,"sriram@employee.com")
employee_2.access_email()
employee_2.order_food('MCDonalds')
info_2 = employee_2.employee_info()
# We mention () when calling a function it means run as a function. - vague explanation - clarity needed.........
print(info_2)

# To understand __str__ # Comment __str__ special method and then uncomment and try.
print(employee_1)
print(employee_2)
# With commented __str__
# Outputs: Memory locations: <__main__.Employees object at 0x000001B7917D3FD0>,<__main__.Employees object at 0x000001B7917D3EE0>
# With uncommented __str__
# You get in this format: employee_info = f"name: {self.name}, age: {self.age}, phone number employee: {self.phone_number}, email id employee: {self.email_id}, position in the organisation: {self.position}"

# To understand __eq__ # Comment __eq__ special method and then uncomment and try.
employee_3 = Employees('biologist','Sriram',16,111111111,2500,"sriram@employee.com")

print(employee_2 == employee_3)
# With commented __str__
# Output: False (Because it compares the memory addresses.........)
# With uncommented __str__
# Output: True (Because it follows the instructions in  __eq__.........)

# Accessing static method 
print(Employees.calculate_entry_salary(26)) # Can be accessed by class.
print(employee_3.calculate_entry_salary(28)) # Can be accessed by instance as well.

# Final conclusion:
# 1. Instance methods need self which is the instance itself as the first argument.
# 2. Many other arguments can be passed other than self and instance methpds can return values using return statement.
# 3. Special "dunder" built in methods in Python. Eg: __str__ and __eq__
# 4. Static methods can be used with @staticmethod, it cannot use instance attributes because it does not pass the instance nor the class.
