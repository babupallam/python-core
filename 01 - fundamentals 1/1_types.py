
# Python Data Types
# ==================
# build in types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType



x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType	

#==========================================
#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#==========================================
#float
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#==========================================
#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#==========================================
#type conversion: using methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))#<class 'float'>
print(type(b))#<class 'int'>
print(type(c))#<class 'complex'>
#==========================================
#generating random number:

# python doesnt have method for that, but it does have inbuild module that does iter

import random
print(random.random())#0.518615995335651
print(random.randrange(1,10))#in between 1 and 9
#==========================================
#strings
a="babu"
b=str("babu")
#multiline
c="""Im going to
write a multi
line para into 
a varibale named
c
"""
print(a)
print(b)
print(c)

print(a==b)#true
# print(a===b)# error

#==========================================
#Boolean Values
#True or False

x= bool(0)
print(x)#False

print(bool("Hello"))#True
print(bool(15))#True

bool(False)#False
bool(None)#False
bool(0)#False
bool("")#False
bool(())#False
bool([])#False
bool({})#False