'''
int 
float 
complex 
bool
'''
a = 10          # int
b = 3.14        # float
c = 2 + 3j     # complex
d = True       # bool

print(type(a))
print(type(b))
print(type(c))

#type conversion
x = 5           # int
y = float(x)    # convert int to float
z = complex(x)  # convert int to complex
w = int(b)      # convert float to int
v = bool(1)     # convert int to bool
print(y)
print(z)
print(w)
print(v)
print(type(y))
print(type(z))
print(type(w))
print(type(v))
print("---------")

#Random Number Generation
import random
print(random.randint(1, 100))  # Random integer between 1 and 100
print(random.uniform(1.0, 10.0)) # Random float between 1.0 and 10.0
print("---------")
