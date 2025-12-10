print("Strings")                                #Strings
print("he is called 'johnny' ")

a = "Hello" 
print(a)

b = """multiple comments can added through      
this type
of triple quotation so use it oftenly"""        #Multiple String
print(b)

c = "I am Back"                                 #string are arrays
print(c[0:9])

for d in "greatest of all time":                #for looping
    print(d)

d = "Legend was born"                           #to find length
print(len(d))

txt = "the best thing in life are free"         #if statement
if "free" in txt:
    print("yes,'free' is present")

text = "the best thing in life are free"        #if not statement
if "expensive" not in text:
    print("No, 'expensive' is NOT present.")

e = "always go with precision"                  #Slicing
print(e[2:9])

f = "believe in your dreams"                    #Slice From Start
print(f[:5])

f = "believe in your dreams"                    #Slice From End
print(f[2:])

g = "just do it"                                #Negative Indexing
print(g[-5:-2])

h = "Aggresion and ego goes hand to hand"       #Upper Case
print(h.upper())                            

i = "Aggresion and ego goes hand to hand"       #Lower Case
print(i.lower())                            

j = "  basics are always important   "
print(j.strip())                                #Remove whitespaces

k = "Love the way you lie"
print(k.replace("lie","smile"))                 #replace String

l = "always with, you"
print(l.split(","))                             #returns ['always with','you']

a = "i can"
b = "i will"
c = a + " " + b
print(c)                                        #concatination

age = 32
txt = f'My name is john, i am {age}'
print(txt)                                      #f-string

price = 76
txt = f"The price is {price:.2f} dollars"
print(txt)                                      #Placeholders and modifiers

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "we are the so-called \"vikings\" from the north"
print(txt)

