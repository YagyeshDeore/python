'''python Functions
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.
'''
def greet(name):
    """This function greets to the person passed in as a parameter"""
    print("Hello, " + name + ". Good morning!")

greet('Paul')


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


def get_greeting():
  return "Hello from a function"

print(get_greeting())

#python Function Arguments
def greet(name, msg):
    """This function greets to the person with the provided message"""
    print("Hello, " + name + ', ' + msg)
greet("Monica", "Good morning!")
greet("John", "How do you do?")
#Keyword Arguments
greet(msg="Welcome!", name="Kate")
#Default Parameter Value
def greet(name, msg="Good morning!"):
    """This function greets to the person with the provided message"""
    print("Hello, " + name + ', ' + msg)
greet("Kate")  # uses default value
greet("Bruce", "How do you do?")  # uses provided value
#Passing a List as an Argument
def greet_names(names):
    """This function greets all the names in the list"""
    for name in names:
        print("Hello, " + name)
list_of_names = ["Monica", "Luke", "Steve"]
greet_names(list_of_names)
#Python Anonymous Functions
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Syntax
#lambda arguments : expression
#The expression is executed and the result is returned
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))
print(mytripler(5))
#Python - Map Function
#The map() function executes a specified function for each item in an iterable.
#The item is sent to the function as a parameter.
def myfunc(n):
    return len(n)
names = ['John', 'Paul', 'George', 'Ringo']
result = map(myfunc, names)
print(list(result))
#Using lambda function
names = ['John', 'Paul', 'George', 'Ringo']
result = map(lambda n: len(n), names)
print(list(result))
#Python - Filter Function
#The filter() function creates a list of elements for which a function returns true.
def myfunc(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
result = filter(myfunc, numbers)
print(list(result))
#Using lambda function
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda n: n % 2 == 0, numbers)
print(list(result))


#Python - Function Arguments - Keyword vs Positional

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

my_function("cat", "Whiskers")
my_function("parrot", name = "Polly")
my_function(animal = "fish", name = "Goldie")
my_function("hamster", "Nibbles")
#Note: If you mix positional and keyword arguments, the positional arguments must come first.
#This will result in a syntax error:
#my_function(name = "Buddy", "dog")  # This will cause an error
#Correct way:
my_function("dog", name = "Buddy")
#Python - Function Annotations
def greet(name: str) -> str:
    return "Hello, " + name
print(greet("Alice"))
print(greet.__annotations__)
def add(a: int, b: int) -> int:
    return a + b
print(add(5, 3))
print(add.__annotations__)
def multiply(a: float, b: float) -> float:
    return a * b
print(multiply(2.5, 4.0))
print(multiply.__annotations__)
def divide(a: int, b: int) -> float:
    return a / b
print(divide(10, 2))
print(divide.__annotations__)
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent
print(power(3))
print(power(2, 3))
print(power.__annotations__)
def concatenate(str1: str, str2: str) -> str:
    return str1 + str2
print(concatenate("Hello, ", "World!"))
print(concatenate.__annotations__)
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial.__annotations__)
def greet(name: str, msg: str = "Good morning!") -> str:
    return "Hello, " + name + ', ' + msg
print(greet("Kate"))
print(greet("Bruce", "How do you do?"))
print(greet.__annotations__)
#Python - Docstrings
def add(a, b):
    """Return the sum of a and b."""
    return a + b
print(add(3, 5))
print(add.__doc__)
def factorial(n):
    """Return the factorial of n, an integer >= 0."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial.__doc__)
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))
print(fibonacci.__doc__)
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime.__doc__)
def greet(name):
    """Return a greeting message for the given name."""
    return "Hello, " + name + "!"
print(greet("Alice"))
print(greet.__doc__)
def square(n):
    """Return the square of a number n."""
    return n * n
print(square(4))
print(square.__doc__)
def reverse_string(s):
    """Return the reverse of the input string s."""
    return s[::-1]
print(reverse_string("hello"))
print(reverse_string.__doc__)
def calculate_area(radius):
    """Return the area of a circle given its radius."""
    import math
    return math.pi * radius * radius
print(calculate_area(5))
print(calculate_area.__doc__)
def find_maximum(lst):
    """Return the maximum value from a list lst."""
    return max(lst)
print(find_maximum([3, 1, 4, 1, 5, 9]))
print(find_maximum.__doc__)
def count_vowels(s):
    """Return the number of vowels in the input string s."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello World"))
print(count_vowels.__doc__)
def greet(name):
    """This function greets to the person passed in as a parameter"""
    print("Hello, " + name + ". Good morning!") 


def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")