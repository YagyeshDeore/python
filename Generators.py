#Generators
def my_generator():
    yield 1
    yield 2
    yield 3 
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))   
for value in my_generator():
    print(value)    
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
for num in counter:
    print(num)
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))
def even_numbers(n):
    for num in range(n):
        if num % 2 == 0:
            yield num
evens = even_numbers(10)
for even in evens:
    print(even)
def prime_generator(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
primes = prime_generator(20)
for prime in primes:
    print(prime)
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)
def squares(n):
    for i in range(n):
        yield i * i
for square in squares(10):
    print(square)
def infinite_ones():
    while True:
        yield 1
ones = infinite_ones()
for _ in range(5):
    print(next(ones))
def alternating_generator():
    while True:
        yield 'A'
        yield 'B'
alt_gen = alternating_generator()
for _ in range(6):
    print(next(alt_gen))
def power_generator(base, n):
    for exp in range(n):
        yield base ** exp
for power in power_generator(2, 5):
    print(power)
def reverse_string_generator(s):
    for char in reversed(s):
        yield char
for char in reverse_string_generator("hello"):
    print(char)
def flatten_list(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item
nested = [[1, 2], [3, 4], [5]]
for item in flatten_list(nested):
    print(item)
def factorial_generator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact
for fact in factorial_generator(5):
    print(fact)
def collatz_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1
for number in collatz_generator(6):
    print(number)
def sliding_window_generator(lst, size):
    for i in range(len(lst) - size + 1):
        yield lst[i:i + size]
for window in sliding_window_generator([1, 2, 3, 4, 5], 3):
    print(window)
def unique_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item
for unique in unique_generator([1, 2, 2, 3, 4, 4, 5]):
    print(unique)
def digit_generator(n):
    for digit in str(n):
        yield int(digit)
for digit in digit_generator(12345):
    print(digit)
def matrix_generator(matrix):
    for row in matrix:
        for item in row:
            yield item
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in matrix_generator(matrix):
    print(item)
def repeating_generator(value):
    while True:
        yield value
rep_gen = repeating_generator("Hello")
for _ in range(3):
    print(next(rep_gen))
def cumulative_sum_generator(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        yield total
for cum_sum in cumulative_sum_generator(5):
    print(cum_sum)
def zigzag_generator(list1, list2):
    for a, b in zip(list1, list2):
        yield a
        yield b
for item in zigzag_generator([1, 3, 5], ['a', 'b', 'c']):
    print(item)
def hamming_generator():
    yield 1
    multiples_of_2 = [2]
    multiples_of_3 = [3]
    multiples_of_5 = [5]
    hamming_numbers = [1]
    while True:
        next_hamming = min(multiples_of_2[0], multiples_of_3[0], multiples_of_5[0])
        yield next_hamming
        hamming_numbers.append(next_hamming)
        if next_hamming == multiples_of_2[0]:
            multiples_of_2.append(next_hamming * 2)
            multiples_of_2.pop(0)
        if next_hamming == multiples_of_3[0]:
            multiples_of_3.append(next_hamming * 3)
            multiples_of_3.pop(0)
        if next_hamming == multiples_of_5[0]:
            multiples_of_5.append(next_hamming * 5)
            multiples_of_5.pop(0)
hamming_gen = hamming_generator()
for _ in range(10):
    print(next(hamming_gen))
def pascal_triangle_generator():
    row = [1]
    while True:
        yield row
        row = [sum(pair) for pair in zip([0]+row, row+[0])]
pascal_gen = pascal_triangle_generator()
for _ in range(5):
    print(next(pascal_gen))
def prime_factors_generator(n):
    factor = 2
    while n > 1:
        while n % factor == 0:
            yield factor
            n //= factor
        factor += 1
for factor in prime_factors_generator(56):
    print(factor)
def look_and_say_generator():
    term = "1"
    while True:
        yield term
        next_term = ""
        i = 0
        while i < len(term):
            count = 1
            while i + 1 < len(term) and term[i] == term[i + 1]:
                i += 1
                count += 1
            next_term += str(count) + term[i]
            i += 1
        term = next_term
look_and_say_gen = look_and_say_generator()
for _ in range(5):
    print(next(look_and_say_gen))
def pascal_triangle_generator():
    row = [1]
    while True:
        yield row
        row = [sum(pair) for pair in zip([0]+row, row+[0])]
pascal_gen = pascal_triangle_generator()
for _ in range(5):
    print(next(pascal_gen))
def prime_factors_generator(n):
    factor = 2
    while n > 1:
        while n % factor == 0:
            yield factor
            n //= factor
        factor += 1
for factor in prime_factors_generator(56):
    print(factor)
def look_and_say_generator():
    term = "1"
    while True:
        yield term
        next_term = ""
        i = 0
        while i < len(term):
            count = 1
            while i + 1 < len(term) and term[i] == term[i + 1]:
                i += 1
                count += 1
            next_term += str(count) + term[i]
            i += 1
        term = next_term
look_and_say_gen = look_and_say_generator()
for _ in range(5):
    print(next(look_and_say_gen))   
    