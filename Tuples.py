mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))
print(len(mytuple))
# Output:
# ('apple', 'banana', 'cherry')
# <class 'tuple'>
# A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.
#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
# Output:
# ('apple', 'banana', 'cherry')
print(len(thistuple))
# Output:
# 3

#negative indexing
print(mytuple[-1])
# Output:
# cherry
print(mytuple[-3])
# Output:
# apple
#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
# Output:
# ('apple', 'banana', 'cherry')
# (1, 5, 7, 9, 3)
# (True, False, False)
# ('abc', 34, True, 40, 'male')
#The tuple() Constructor can be used to make a tuple
tuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple5)
# Output:
# ('apple', 'banana', 'cherry') 
#Python - Unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Output:
# apple
# banana
# cherry
#Using Asterisk* When Unpacking Tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# Output:
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']
#Looping Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# Output:
# apple
# banana
# cherry
#Looping Through the Index Numbers