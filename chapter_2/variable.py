#Rules for vaiable names
#Python vaiable names must begin with a letter or an underscore _ character

name = "Robert"
age = 30

#TypeError: cannot concatenate 'str' and 'int' objects
#print(name + ' is ' + age + ' years old')

# Python Data Types
""" numeric
iterator
sequence
mapping
file
class
exception """

# 3 Numerical Data Type: int / float / complex
a = 12
b = 3 
print(a + b) #15
print(a - b) #9
print(a * b) #36
print(a / b) # 4.0
print(a // b) # 4 integer division, rounded down towards minus infinity
print(a % b) # 0 modulo: the remainder after integer division

print("\n")

for i in range(1,4):
    print(i)

print("\n")

for i in range(1, a//b):
    print(i)