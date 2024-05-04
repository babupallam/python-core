# Python:
#     - high level, general purpous, 
#     - used for web development, software development, mathematics, system scripting
#     - why python:
#         - works in different platforms
#         - syntax is similar to english langugae, more highlevel language
#         - used to handle big data and complex maths
#         - Python can be used for rapid prototyping, or for production-ready software development.
#         - Python can be treated in a procedural way, an object-oriented way or a functional way
#     - modern version is python 3

print ("hello world")
#==========================================

# ob1: intentation in python is very important, 
#     otherwise it will produce error

if(5>2):
    print("all is good")
#==========================================

#ob2: multiline comment
"""
THis all will
get commented during
exicution
"""
#==========================================

#variables
# ============
#loosly prototyped
x=5;# type int
y="salary"#type str
#==========================================


#by using typecasting
x = str(3)    # x will be '3'  
y = int(3)    # y will be 3     
z = float(3)  # z will be 3.0   <class 'float'>

print(type(x))#<class 'str'>
print(type(y))#<class 'int'>

#==========================================

#ob3: no difference with single quote or double quote
x="babu"
y='babu'
#both are same

#==========================================
#variable naming:
    # - begin with letter or underscore
    # - can contain alpha numaric and underscrore
    # - name should not be any python keyword

#multiword variable name
#1. Camel case: myVaribleName ="this"
#1. Phascal case: MyVaribleName ="this"
#1. Snake case: my_variable_name ="this"

#==========================================
# variable assignation
x,v,z ="one","two", 34
print(x,y,z)#one babu 34

#==
a=b=c=34#allowed
#==
fruits = ["apple", "banana","cherry"]
x,y,z = fruits
print(x,y,z)#apple banana cherry
#==
# dynamic type casting is not there in python
x,y=5,10;
print(x+y) # 15
i,j=5,"babu"
# print(i+j)# error
# print(j+i)# error
# print(i,j)#5babu --- valid
#==========================================

#global keyword
# ===============
def myFun():
    global x
    x="babu"
myFun()
print("x is ", x) # x is  babu

#===
y="global"
def myFun():
    y=45
    print("y from fun: ",y) #y from fun:  45
myFun()
print("y from global scope: ",y) # y from global scope:  global

#==========================================
