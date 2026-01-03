#Scope
x = "global x" #global variable
def my_function():
    y = "local y" #local variable
    print(x)  #accessing global variable inside function
    print(y)  #accessing local variable inside function
my_function()
print(x)  #accessing global variable outside function
#print(y)  #this will raise an error as y is not defined outside the function
#To modify a global variable inside a function, use the 'global' keyword
z = "global z"
def modify_global():
    global z
    z = "modified global z"
modify_global()
print(z)  #prints "modified global z"
#Nested function scope
def outer_function():
    outer_var = "outer variable"
    def inner_function():
        inner_var = "inner variable"
        print(outer_var)  #accessing outer function's variable
        print(inner_var)  #accessing inner function's variable
    inner_function()
    #print(inner_var)  #this will raise an error as inner_var is not defined in outer_function
outer_function()
#LEGB Rule
#Local, Enclosing, Global, Built-in
x = "global x"
def outer():
    x = "enclosing x"
    def inner():
        x = "local x"
        print(x)  #prints "local x"
    inner()
    print(x)  #prints "enclosing x"
outer()
print(x)  #prints "global x"
#Built-in scope example
print(len("Hello"))  #len is a built-in function
def len(s):
    return "This is a custom len function"
print(len("Hello"))  #calls the custom len function
#To access the built-in len function, use the builtins module
import builtins
print(builtins.len("Hello"))  #calls the built-in len function
#Function scope with loops
def loop_function():
    for i in range(5):
        print(i)  #prints numbers from 0 to 4
    #print(i)  #i is accessible here, prints 4
loop_function()
#However, it's good practice to avoid relying on loop variables outside their intended scope
#Using nonlocal keyword
def outer_function_nonlocal():
    var = "outer variable"
    def inner_function_nonlocal():
        nonlocal var
        var = "modified outer variable"
    inner_function_nonlocal()
    print(var)  #prints "modified outer variable"
outer_function_nonlocal()
#Lambda function scope
x = 10
add_x = lambda y: x + y
print(add_x(5))  #prints 15 
#If x is redefined inside a function, the lambda will still refer to the global x
def redefine_x():
    x = 20
    add_x_inner = lambda y: x + y
    print(add_x_inner(5))  #prints 25
redefine_x()
print(add_x(5))  #still prints 15
#Global constants
PI = 3.14159
def calculate_circumference(radius):
    return 2 * PI * radius
print(calculate_circumference(5))  #prints circumference for radius 5
#Avoiding global variable conflicts
def function_one():
    global var
    var = "function one variable"
function_one()
print(var)  #prints "function one variable"
def function_two():
    global var
    var = "function two variable"
function_two()
print(var)  #prints "function two variable"
#To avoid such conflicts, use function parameters and return values instead of global variables
def function_one_safe():
    var = "function one variable"
    return var
def function_two_safe():
    var = "function two variable"
    return var
var1 = function_one_safe()
var2 = function_two_safe()
print(var1)  #prints "function one variable"
print(var2)  #prints "function two variable"    


#Decorators and scope
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function 
@decorator_function
def display():
    print("Display function executed")
display()