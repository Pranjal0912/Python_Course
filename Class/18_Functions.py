#=========================
# FUNCTIONS IN PYTHON:
#=========================

# - A function is a block of code that performs a specific task. 
# - It can take input parameters, perform operations, and return output values.
# - Functions help in code reusability, modularity, and organization.

# - Python provides built-in functions like print(), len(), type(), etc., and also allows users to define their own functions using the def keyword.
# - Python functions are generally used/called in 3 ways:

# 1. obj.method()
# -> Methods: functions that belong to a specific class/object.
# -> Example: string.upper(), list.append()

# 2. function(obj)
# -> General/global built-in functions.
# -> Work on many data types and are directly available in Python.
# -> Example: len(), type(), print(), input(), sorted()

# 3. module.function(obj)
# -> Functions stored inside modules/libraries.
# -> Modules help organize related functionality.
# -> Example: math.sqrt(), re.search(), random.randint()

# Key Difference:
# -> Methods belong to objects/classes.
# -> Built-in functions belong to Python's global built-in namespace.
# -> Module functions belong to imported modules/libraries.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------

#=========================
# STRUCTURE OF A FUNCTION:
#=========================

#1. Writing a function:

# - A function is defined using the def keyword, followed by the function name, parentheses (which may include parameters), and a colon.
# - The function body is indented and contains the code to be executed when the function is called.
# - It can optionally return a value using the return statement.
# Syntax:

            # def function_name(parameters): ---> This is also called the function signature.
            #     """docstring (optional)"""
            #     # function body
            #     return value (optional)

# Example:
# A. 
def greet(name):
    """This function greets the person with the provided name."""
    return f"Hello, {name}!"

# B.
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# C.
def is_even(num):
    """This function checks if a number is even or odd but does not return any value."""
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Calling a function:

# - A function is called by using its name followed by parentheses. If the function requires parameters, they are passed inside the parentheses.
# - The function executes its code and returns a value if specified or performs an action if it does not return a value.
# Example: 
greeting = greet("Pranjal") # -> This function returns a value, so we can store it in a variable.
print(greeting) # -> Output: Hello, Pranjal!
sumation = add_numbers(5, 10) # -> Similarly, this function returns a value, so we can store it in a variable.
print(sumation) # -> Output: 15
is_even(7) # -> Now, this function does not return any value, it just prints the result directly.

# Now in a function :
                            # def abc(Formal parameters):
                            #     << body >>

                            # abc(Actual parameters)

                            # - Actual parameters are the values passed to the function when it is called.
                            # - Formal parameters are the variables defined in the function signature that receive the values of the actual parameters.

                # - Whatever value is passed to the function during the function call, those values are refferenced by the formal parameters inside the function body.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Positional and Keyword Arguments:

# - consider the following function as an example:

def volume(length, width, height):
    """This function calculates the volume of a cuboid."""
    vol = length * width * height
    return vol

# let's call the function using positional arguments:

vol1 = volume(5, 3, 2) # -> Here, the values 5, 3, and 2 are passed as positional arguments to the function. 
    # 1st value: 5 -> assigned to 1st parameter 'length'
    # 2nd value: 3 -> assigned to 2nd parameter 'width'
    # 3rd value: 2 -> assigned to 3rd parameter 'height'

# - Positional arguments are arguments that are passed to a function in the order in which they are defined in the function signature. The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.

# lets call the function using keyword arguments:

vol2 = volume(length=5, height=2, width=3) # -> Here, the values are passed as keyword arguments to the function.
    # value 5 is assigned to parameter 'length'
    # value 2 is assigned to parameter 'height'
    # value 3 is assigned to parameter 'width'

    # So here the values are assigned based on the parameter names that are specified in the function call, rather than their position in the argument list. ( See how despite changing the order of the arguments, the values are still assigned to the correct parameters based on their names.)

# - Keyword arguments are arguments that are passed to a function by explicitly specifying the parameter name along with its value. This allows for more flexibility in the order of arguments and makes the code more readable.

# Can we mix positional and keyword arguments in a function call?
# - Yes, we can mix positional and keyword arguments in a function call, but there are some rules to follow:
    # 1. Positional arguments must always come before keyword arguments in the function call.
    # 2. Once a keyword argument is used, all subsequent arguments must also be keyword arguments

# let's see an example of mixing positional and keyword arguments:
vol3 = volume(5, width=3, height=2) # -> Here, we are mixing positional and keyword arguments.
    # 1st value: 5 -> assigned to 1st parameter 'length' (positional argument)
    # value 3 is assigned to parameter 'width' (keyword argument)
    # value 2 is assigned to parameter 'height' (keyword argument)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Default Arguments:

# lets take 'index()" for example, its signature was -> index(substring, start, end) 
#   - Here, 'start' and 'end' are optional parameters with default values. If we do not provide values for these parameters, the function will use the default values. These were Default arguments.
#   - Default arguments are parameters that have a default value specified in the function signature. If the caller does not provide a value for that parameter, the default value is used. 
# Example:
def greet(name, msg="Hello"): # -> Here, 'msg' is a default argument with a default value of "Hello". If we do not provide a value for 'msg' when calling the function, it will use the default value.
    """This function greets the person with the provided name and message."""
    print(f"{msg}, {name}!")

greet("Alice")          # -> Uses default message "Hello" Output: Hello, Alice!
greet("Bob", msg="Hi")  # -> When the value of the default argument is provided in the function call it overrides default message with "Hi", which was the actual argument passed to the function. Output: Hi, Bob!

# So comming back to 'index()' function, its actual signature looks like -> index(substring, start=0, end=len(iterable))

# lets now try to make our volume function more flexible by adding default arguments to it:
def volume(length, width=1, height=1): # -> Here, 'width' and 'height' are default arguments with default values of 1. If we do not provide values for these parameters when calling the function, it will use the default values.
    """This function calculates the volume of a cuboid."""
    vol = length * width * height
    return vol

# - Assignment : 
v = volume(5) # -> Here, we are only providing a value for 'length', so the function will use the default values for 'width' and 'height'.
v = volume(5, 3) # -> Here, we are providing values for 'length' and 'width', so the function will use the default value for 'height'.
v = volume(5, 3, 2) # -> Here, we are providing values for all three parameters, so the function will use the provided values.
v = volume() # -> This will raise an error because 'length' is a required parameter and does not have a default value.

# Now one key obeservation is that the assignment of default argument is done from left to right, so if we want to provide a value for 'height' but not for 'width', we have to use keyword arguments:
v = volume(5, height=2) # -> Here, we are providing a value for 'length' and 'height', so the function will use the default value for 'width'.


# - A) Among ordinary positional-or-keyword parameters:
# Once a parameter has a default value, every ordinary parameter after it must also have a default value.

# Valid:
def valid_function(a, b=10, c=20):
    pass

# Invalid:

# def invalid_function(a, b=10, c): -> Error: SyntaxError: non-default argument follows default argument
#     pass

# This restriction prevents ambiguity when positional arguments are supplied. 
# Example: f(12, 20) -> what would the compiler do with the value 20? Should it be assigned to 'b' or 'c'? Hence, this is not allowed.

#Therefore, it is more accurate to say:
# --> "Required ordinary parameters(Non-default) must appear before default ordinary parameters."

# - B) Hetrogeneous default arguments are allowed in Python, meaning that we can have a mix of required and optional parameters in a function signature. However, all required parameters must come before any optional parameters in the function signature.
# Example:

def fun(a=12, b=2.4, c="Hello", d=True, e =[1,2,3]):
    print(a, b, c, d, e)

fun(1,2,3,4,5) # -> Here, we are providing values for all parameters, so the function will use the provided values. This will print "1 2 3 4 5"
fun() # -> Here, we are not providing any values for the parameters, so the function will use the default values. This will print "12 2.4 Hello True [1, 2, 3]"

# - C) Default arguments are only created once when the function is defined, not each time the function is called. This means that if we use a mutable object (like a list or dictionary) as a default argument, and we modify that object inside the function, the default value will be changed for subsequent calls to the function. This can lead to unexpected behavior.
# Let's see an example of this:

def fun(l=[1,2,3]):
    """ This function appends the length of the list to the list itself."""
    l.append(len(l))
    print(l)

# 1st call to the function with no arguments, so the default list [1, 2, 3] is used. The length of the list is 3, so 3 is appended to the list. The function prints [1, 2, 3, 3].
fun() # -> This will print "[1, 2, 3, 3]", Now the default list has been modified from [1, 2, 3] to [1, 2, 3, 3].

# 2nd call to the function with no arguments, so the modified default list [1, 2, 3, 3] is used. The length of the list is now 4, so 4 is appended to the list. The function prints [1, 2, 3, 3, 4].
fun() # -> This will print "[1, 2, 3, 3, 4]", Now the default list has been modified from [1, 2, 3, 3] to [1, 2, 3, 3, 4].

# 3rd call to the function but this time with argument, so the default list is not used.
fun([10, 20, 30]) # -> This will print "[10, 20, 30, 3]", Now the default list is not modified because we provided a new list as an argument.

# 4th call to the function with no arguments, so the modified default list [1, 2, 3, 3, 4] is used. The length of the list is now 5, so 5 is appended to the list. The function prints [1, 2, 3, 3, 4, 5].
fun() # -> This will print "[1, 2, 3, 3, 4, 5]", Now the default list has been modified from [1, 2, 3, 3, 4] to [1, 2, 3, 3, 4, 5].

# Lets Summarize what we learned about default arguments:
# 1. Default arguments are parameters that have a default value specified in the function signature.
# 2. If the caller does not provide a value for that parameter, the default value is used.
# 3. Default arguments are only created once when the function is defined, not each time the function is called, hence if a mutable object (like a list or dictionary) is used as a default argument, and it is modified inside the function, the default value will be changed for subsequent calls to the function.
# 4. They are assigned from right to left, meaning that all required parameters must come before any optional parameters in the function signature.
# 5. They can be of any data type (Heterogeneous).

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Positional-only Arguments:

# - Positional-only arguments are parameters that can only be specified by their position in the function call, and cannot be specified by their name. 
# - They are defined in the function signature using a forward slash (/) to indicate that all parameters before the slash are positional-only.
# Example:
def fun(a, b, /, c, d):  # --> a and b are positional-only arguments, while c and d can be specified by name or position.
    print(a, b, c, d)

fun(1, 2, 3, 4) # -> This will print "1 2 3 4"
fun(a=1, b=2, c=3, d=4) # -> This will raise a TypeError because a and b are positional-only arguments.

# lets see some possible signatures of functions with positional-only arguments:
def fun1(a, b, /): # -> Here, a and b are positional-only arguments.
    pass
def fun2(a, b, /, c): # -> Here, a and b are positional-only arguments, while c can be specified by name or position.
    pass
# def fun3(/,a, b, c): # -> This is not a valid signature because the forward slash (/) must come after at least one parameter.
    # pass

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Keyword-only Arguments:

# - Keyword-only arguments are parameters that can only be specified by their name in the function call, and cannot be specified by their position.
# - They are defined in the function signature using an asterisk (*) to indicate that all parameters after the asterisk are keyword-only.
# Example:  

def fun(a, b, *, c, d):  # --> a and b can be specified by name or position, while c and d are keyword-only arguments.
    print(a, b, c, d)

fun(1, 2, c=3, d=4) # -> This will print "1 2 3 4"
fun(a=1, b=2, c=3, d=4) # -> This will also print "1 2 3 4"
fun(1, 2, 3, 4) # -> This will raise a TypeError because c and d are keyword-only arguments and must be specified by name.

# lets see some possible signatures of functions with keyword-only arguments:
def fun1(a, b, *, c): # -> Here, a and b can be specified by name or position, while c is a keyword-only argument.
    pass    
def fun2(*, a, b): # -> Here, a and b are keyword-only arguments.
    pass
# def fun3(a, b, c, d, *): # -> This is not a valid signature because the asterisk (*) must come before at least one parameter.
    # pass

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Positional-only and Keyword-only Arguments:

# - A function can have both positional-only and keyword-only arguments, as well as regular arguments that can be specified by name or position.
# - The positional-only arguments must come before the forward slash (/), the regular arguments can come after the forward slash and before the asterisk (*), and the keyword-only arguments must come after the asterisk.
# Example:

def fun(a, b, /, c, *, d, e):  # --> a and b are positional-only arguments, c can be specified by name or position, while d and e are keyword-only arguments.
    print(a, b, c, d, e)

fun(1, 2, 3, d=4, e=5) # -> This will print "1 2 3 4 5"

# lets see some possible signatures of functions with both positional-only and keyword-only arguments:
def fun1(a, b, /, *, c): # -> a and b are positional-only arguments, c is a keyword-only argument.
    pass
def fun2(a, b, /, *, c, d): # -> a and b are positional-only arguments, c and d are keyword-only arguments.
    pass
# def fun3(a, b, *, /, c, d): # -> This is not a valid signature because the forward slash (/) must come before the asterisk (*).


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Variable-length Arguments:

# lets take an example of 'print()' function:
# Now 'print()' function can take any number of arguments, and it will print them all. 
print("Hello", "World", "!", 1, 2, 3) # -> This will print "Hello World ! 1 2 3" --> Here the number of arguments(objects) is 6.
print("Hello", "World") # -> This will print "Hello World" -> Here the number of arguments(objects) is 2.

# 'print()' is an example of a function that takes variable-length arguments.
# - Variable-length arguments allow a function to accept any number of arguments, which can be useful when the number of inputs is not known in advance.
# - In Python, we can define a function that takes variable-length arguments using the *args and **kwargs syntax.
# - The *args syntax allows a function to accept any number of positional arguments. The **kwargs syntax allows a function to accept any number of keyword arguments.

# A. Variable-length Positional Arguments (*args):

# - The *args syntax allows a function to accept any number of positional arguments.
# - The arguments are passed to the function are collected into a tuple, which can be accessed inside the function.
# Example:

def fun(*args):
    """This function takes any number of positional arguments and prints them."""
    print(args)

fun(1, 2, 3) # -> This will print "(1, 2, 3)"
fun("Hello", "World") # -> This will print "('Hello', 'World')
fun(1) # -> This will print "(1,)"

# Now the question arises, Can I have more arguments along with *args in a function signature?
# - Yes, we can have more arguments along with *args in a function signature. However, there are some rules to follow:
# 1. If arguments are specified before *args, they must be passed as positional arguments only when calling the function. 
# 
# Example:
def fun(a, b, *args):
    """This function takes two regular positional arguments and any number of additional positional arguments."""
    print(a, b, args)

fun(10, 20, 30) # -> This will print "10 20 (30,)" Because 10 is assigned to a, 20 is assigned to b, and 30 is collected into the args tuple.

# 2. If arguments are specified after *args, they must be passed as keyword arguments only when calling the function. ( Why? Because if we pass them as positional arguments, they will be collected into the args tuple, and the function will not be able to access them as separate arguments.)
# Example:
def fun(a, b, *args, c, d):
    """This function takes two regular positional arguments, any number of additional positional arguments, and two keyword-only arguments."""
    print(a, b, args, c, d)

fun(1, 2, 3, c=10, d=20) # -> This will print "1 2 (3,) 10 20" -> Here 1 is assigned to a, 2 is assigned to b on the basis of position, 3 is collected into the args tuple, and 10 and 20 are assigned to c and d on the basis of keyword.
fun(1, 2, 3, 4, 5) # -> This will raise a TypeError because c and d are keyword-only arguments and must be specified by name.


# Now suppose if we pass a single list (or a tuple) as an argument to the function, then it will be treated as a single positional argument and will be collected into the args tuple as a single element.
def fun(*args):
    """This function takes any number of positional arguments and prints them."""
    print(args)
l1 = [1, 2, 3]
fun(l1) # -> This will print "([1, 2, 3],)" -> Here the list [1, 2, 3] is treated as a single positional argument and is collected into the args tuple as a single element.
# But if we want to pass the elements of the list (or tuple) as separate positional arguments, we can use the unpacking operator (*) to unpack the list (or tuple) into separate arguments. --> REMEMBER : We learned about unpacking in the previous class (Class/15_Tuple.py)
fun(*l1) # -> This will print "(1, 2, 3)" -> Here the list [1, 2, 3] is unpacked into separate positional arguments and is collected into the args tuple as separate elements.


# B. Variable length Keyword Arguments (**kwargs):

#  - The **kwargs syntax allows a function to accept any number of keyword arguments.
#  - The arguments passed to the function are collected into a dictionary, which can be accessed inside the function.
# Example:

def fun(**kwargs):
    """This function takes any number of keyword arguments and prints them."""
    print(kwargs)
    for k,v in kwargs.items(): # This will iterate over the key-value pairs of the dictionary using the 'items()' method.
        print(k, f' : {v}') # Output: Name: John, Age: 30, City: New York -> This will print the key and its corresponding value in the dictionary.

fun(a=1, b=2, c=3) # -> This will print "{'a': 1, 'b': 2, 'c': 3}" -> Here the keyword arguments are collected into the kwargs dictionary.
fun(name="Alice", age=30) # -> This will print "{'name': 'Alice', 'age': 30}" -> Here the keyword arguments are collected into the kwargs dictionary.

# Now just like *args, we can have more arguments along with **kwargs in a function signature. There is just one rule to follow:

# 1. **kwargs must be the last parameter in the function signature and p 
# => This is because any parameters that come after **kwargs will not be able to accept any keyword arguments, as all keyword arguments will be collected into the kwargs dictionary and a positional argument cannot be passed after a keyword argument. Hence, it is not possible to have any parameters after **kwargs in the function signature.
# Example:

def fun(a, b, **kwargs):
    """This function takes two regular positional arguments and any number of additional keyword arguments."""
    print(a, b, kwargs)

fun(1, 2, c=3, d=4) # -> This will print "1 2 {'c': 3, 'd': 4}" -> Here 1 is assigned to a, 2 is assigned to b on the basis of position, and c and d are collected into the kwargs dictionary.
fun(1, 2, 3) # -> This will raise a TypeError because 3 is a positional argument and cannot be passed into the kwargs dictionary. 
fun(1,2, c=3, d=4, e=5) # -> This will print "1 2 {'c': 3, 'd': 4, 'e': 5}" -> Here 1 is assigned to a, 2 is assigned to b on the basis of position, and c, d and e are collected into the kwargs dictionary.

#def fun(a, b, **kwargs, c):
"""This function takes two regular positional arguments, any number of additional keyword arguments, and a required keyword-only argument."""
    # print(a, b, kwargs, c)

#fun(1, 2, m =10, d = 12, c=3) # -> So even though this might make sense to us, this will raise a SyntaxError because by defination, **kwargs must be the last parameter in the function signature.

# C. General Form of a Function Signature:

# => A usefull general form of a function signature that can accept any number of positional and keyword arguments is as follows:
def fun(a, b, *args, c, d, **kwargs):
    pass
# In here:
# - a and b are regular positional arguments.
# - *args collects any additional positional arguments into a tuple.
# - c and d are required keyword-only arguments. (because they come after *args)
# - **kwargs collects any additional keyword arguments into a dictionary.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Multiple Return Values:
# => In Python, a function can return multiple values as a tuple.
# Example:

def fun():
    a = 1
    b = 2
    c = 3
    return a, b, c

print(fun()) # -> This will print "(1, 2, 3)" -> Here the function returns a tuple containing the values of a, b, and c.
print(type(fun())) # -> This will print "<class 'tuple'>" -> Here the function returns a tuple containing the values of a, b, and c.
x, y, z = fun() # -> This will assign 1 to x, 2 to y, and 3 to z.
