"""
                  Arithmatic operators 

operator            Name                    Example

+                   Addition                x+y
-                   Substraction            x-y
*                   multiplication          x*y
/                   Division                x/y
%                   Modulus                 x%y
**                  Exponentialism          x**y
//                  Floor Division          x//y
"""

x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print("---------")

""" 
                    Assignment Operators 

operator               Example              Same as

=                      x=3                  x = 3
+=                     x+=3                 x = x + 3
-=                     x-=3                 x = x - 3
/=                     x/=3                 x = x / 3
%=                     x%=3                 x = x % 3
//=                    x//=3                x = x // 3 
**=                    x**=3                x = x ** 3
&=                     x&=3                 x = x & 3    
|=                     x|=3                 x = x | 3
^=                     x^=3                 x = x ^ 3
>>=                    x>>=3                x = x >> 3
<<=                    x<<=3                x = x << 3
:=                     print(x:=3)          x = 3           The walrus operator
                                             print(x)     
"""
#The walrus Operator
numbers = [1,2,3,4,5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

    print("---------")

"""
                  Comparison operators 

operator            Name                    Example

==                  Equal                           x == y
!=                  Not equal                       x != y
>                   Greater than                    x > y
<                   Less than                       x < y
>=                  Greater than or equal to        x >= y
<=                  Less than or equal to           x <= y

"""
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

m = 5                                           #Chaining comparison operator
print("---------")
print(1 < m < 10)
print(1 < m and m < 10)

"""                         Logical Operators


Operator	Description	                                    Example	
and 	    Returns True if both
            statements are true	                            x < 5 and  x < 10	
or	        Returns True if one of
            the statements is true	                        x < 5 or x < 4	
not	        Reverse the result, 
            returns False if the
            result is true	not                             (x < 5 and x < 10)
"""
print("---------")
p = 5

print(p > 0 and p < 10)

q = 5

print(q < 5 or q > 10)

r = 5

print(not(r > 3 and r < 10))
print("---------")
"""
                    Identity Operators

Operator	        Description	                        Example
is 	                Returns True if both                x is y
                    variables are the same
                    object	                            	
is not	            Returns True if both                x is not y
                    variables are not the
                    same object	          
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)                   #The is operator returns True if both variables point to the same object


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)              #The is not operator returns True if both variables do not point to the same object


"""Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal"""
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
print("------------")

"""             Membership Operators    

Operator	        Description	                    Example	
in 	                Returns True if a               x in y
                    sequence with the
                    specified value is
                    present in the object		
not in	            Returns True if a               x not in y
                    sequence with the
                    specified value is
                    not present in the
                    object

"""
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)


text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


print("------------")

"""                         Bitwise Operators

Operator	Name	        Description	                        Example
& 	        AND	            Sets each bit to 1 if               x & y
                            both bits are 1
                                            	
|	        OR	            Sets each bit to 1 if
                            one of two bits is 1	            x | y	

^	        XOR	            Sets each bit to 1 if
                            only one of two bits
                                        is 1	                x ^ y	

~	        NOT	            Inverts all the bits	            ~x	

<<	        Zero fill       Shift left by pushing               x << 2
            left shift	    zeros in from the
                            right and let the
                            leftmost bits fall off		

>>	        Signed right    Shift right by                      x >> 2
            shift	        pushing copies of
                            the leftmost bit in
                            from the left, and 
                            let the rightmost bits
                            fall off	

"""
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print("----------------")

"""
            operator Precedence Order

Operator	                        Description

()	                                Parentheses	
**	                                Exponentiation	
+x  -x  ~x	                        Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                        Multiplication, division, floor division, and modulus	
+  -	                            Addition and subtraction	
<<  >>	                            Bitwise left and right shifts	
&	                                Bitwise AND	
^	                                Bitwise XOR	
|	                                Bitwise OR	

==  !=  >                           Comparisons, identity, and membership operators
>=  <  <= 
is  is not 
in  not in 	                             
	
not	                                Logical NOT	
and	                                AND	
or	                                OR
                     
"""