x = 12 #integer
y = "number" #String
z = 12.87 #float
a = str(3)
b = int(6)
c = float(9.0)

d,e,f, = "Orange","Banana","Apple"

g=h=i= 'orange'

fruits = ["apple","banana","cherry"]
j,k,l = fruits


print(x)
print(y)
print(z)

print(type(a))
print(b)
print(c)

print(d)
print(e)
print(f)

print(g)
print(h)
print(i)

print(j)
print(k)
print(l)

m ="awesome"

def myfunc():
    print("python is " + m)

myfunc()


n = "Great"

def myfunc():
    n = "fantastic"
    print("python is " + n )

myfunc()

print("python is " + n)


def myfunc():
    global o
    o = "love"

myfunc()

print("Python is " + o)

p = "awesome"

def myfunc():
  global p
  p = "fantastic"

myfunc()

print("Python is " + p)