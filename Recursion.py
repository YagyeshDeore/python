#recursion example: factorial calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
# Example usage
print(factorial(5))  # Output: 120
#recursion example: Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
print(fibonacci(6))  # Output: 8
#recursion example: sum of elements in a list
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
# Example usage
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
#recursion example: reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
# Example usage
print(reverse_string("hello"))  # Output: "olleh"
#recursion example: greatest common divisor (GCD)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# Example usage
print(gcd(48, 18))  # Output: 6 