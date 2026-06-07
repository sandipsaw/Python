# What are functions

"""
Functions in Python group reusable code into a block that
can be executed by calling the function name. This helps
avoid repetition and makes programs modular and readable

There are many in-build functions in python like print(), input()
len() etc

But you can create your own function and they are called as
user defined functions. To make your own function you have
to use def keyword and then name the function. After this
you have to call the function using name() and paranthesis.
"""
def greet():
    print("Hello sandip! welcome to python")
greet() # calling the function

# Functions parameters and arguments
"""
First thing I want to talk about is parameters, parameters are
variables listed inside the function definition.
For making the function we have to accept inside the
parenthesis of the function.
"""   
def greet(name): # name is a parameter
    print(f"Hello {name}")
 
"""
Arguments are the Values passed to a function when it is called.
For example you can say you have created the parameters
that are working like variables then we can pass the values to
our variables using arguments
"""
greet('sandip')  # sandip is a Argument

"""
As you can see name is the parameter and Alice is the argument
that we passed to name. And you can pass N number of
parameters and arguments but they must be same like if you
have taken 3 parameters you must have to provide 3 arguments
otherwise there will be error.

And another thing is first parameter, will always capture first
argument and so on. These arguments are called positional
argument.
"""

# Type of arguments
"""
Now there are 3 types of argument that we can pass to
parameters. positional argument, default argument, keyword

argument, For understanding these we will first see examples-
"""

# positional arguments work-
def add(a,b):
    print(f"sum of {a} and {b} is {a+b}")
add(12,74)
add(42,37)

# keyword argument works :- using this you can pass values in any order.

def introduce(name,age):
    print(f"I am {name} and my age is {age}")

introduce(age=23,name='sandip')

# default argument works :- if you don’t pass any value still the function will run-

def greet(name='sandip'):
    print(f"my name is {name}")
greet()
greet('suresh')

# write a program to check a string is palindrome or not byy using function

def palindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]
    if rev == str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
palindrome('NAMAN')
palindrome('RAMAN')

# if you provide return in the function then return sends the value to function and we required to print the function so that it show the answer

def message():
    return 'hello bhai'

print(message())

# In-build data structures
"""Data structures are used to store, organize, and manipulate
data efficiently. Python provides several built-in data
structures
And for storing multiple values we will again use variables
Now in python we have 4 types of in-build data structure
List, Tuple, Dictionary, Set."""

# Custom data structures

"""
Now there are some custom data structures as well like
Stack, Queue, Linked List, Graph etc.
And around these data structures there are some algorithms
like searching algorithms, sorting algorithms.
And this is why the study is called data structures and
algorithm
Lets be clear this python notes are not for the DSA this will
cover all the in-build data structures.
"""

# List Powers
"""
Before starting we need to understand some of the
terminology.
Mutability refers to whether an object's value
can be changed after creation. And List allows this

we know data structures are used to store
multiple values so duplicates means same value occuring
multiple time. List allows this

List maintains ordered data structure maintains
the sequence of elements as they were inserted. This
means you can access elements using their position
(index)

List have heterogenous nature that means
we can have multiple data types inside the list.

mutable - List are  mutable you can change the values of tuple
Duplicate - You can have duplicate values in tuple there are no restriction
Ordered - List are ordered and you can access them through index values
Heterogenous - List also have heterogenous nature and can have different types of data structure in List.
"""

# List Basics

"""A First we have to know what is the syntax of list and how, to create a list we have to use square brackets ([])."""

fruits = ['apple', 'banana', 'orange']

"""
Now list has Indexing and slicing and it is same as string 
The changes we saw in string and list is about mutability, we
can’t change the values of string. but we can change the value of list.
"""
a = [1,2,3,4,5,6,7.5,2,4,True,{},print()]
print(a[2]) # Indexing--> 3 
print(a[1:5:1]) # Slicing --> [2, 3, 4, 5]

a[2] = 10
print(a) 
# Mutability -->  [1, 2, 10, 4, 5, 6, 7.5, 2, 4, True, {}, None]

# List Traversing and methods
"""
Now list traversing is also similar to string traversing it can
be looped using the index values and directly7

Now list has some methods that are used to do many, and
don’t worry if you are not sure what are methods, for now
just think they are like function, further we will see it clearly.
"""
list = [5,12,14,21,26,35]

print(dir(list))
# [append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
for i in range(len(list)):
    print(i)  # print only index

# 1st way using index
for i in range(len(list)):
    print(list[i]) # print list element

# 2nd way using value
for i in list:
    print(i) # print list element

"""Now see some of the examples of the methods you will get it what they are used for."""

number = [5,2,9,1,5,6]

number.append(10) # Add 10 to the end --> [5, 2, 9, 1, 5, 6, 10]
number.insert(2,15)
# Insert 15 at index 2 --> [5, 2, 15, 9, 1, 5, 6, 10]
number.extend([4,8])
# Add multiple element in the end->[5, 2, 15, 9, 1, 5, 6, 10, 4, 8]
number.remove(5) 
# remove the first occurence of list [2, 15, 9, 1, 5, 6, 10, 4, 8]
popped_item = number.pop(3)
# Remove and store the element at idx 3->[2, 15, 9, 5, 6, 10, 4, 8]
index = number.index(6) # find the index of 6 --> 4
count_5 = number.count(5) # count occurence of 5 --> 1
number.sort() 
# Sort the list in asscending order ->[2, 4, 5, 6, 8, 9, 10, 15]
number.sort(reverse=True)
print(number)
# Sort the list in Descending order -> [15, 10, 9, 8, 6, 5, 4, 2]
number.reverse()# Reverse the list order[15, 10, 9, 8, 6, 5, 4, 2]
copy = number.copy() 
print(copy) # Print copy of the list --> [15, 10, 9, 8, 6, 5, 4, 2]
number.clear() # Remove all element from the list --> [ ]
print(number)

## Some Questions on List


# Print positive and negative elements of an List?

c = [15,5,1,-5,14,-85,-41,45]
pos = []
neg = []
print("postive element of list are:-")
for i in c:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)

print("positive element are:",pos)
print("negative element are:",neg)

# Mean of List elements?
d = [4,5,23,74,41,36]
sum = 0
for i in d:
    sum += i
print(f"Average of list : {sum/len(d)}")

# Find the greatest element and print its index too?
greatest = d[0]
index = 0
for i in range(len(d)):
    if d[i] > greatest:
        greatest = d[i]
        index = i
print(f"greatest value of the list is : {greatest} and index is {index}")

# Find the second greatest element?
e = [4,25,62,45,72,68]
largest = e[0]
sec_largest = e[0]
for i in e:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(f"second largest element are : {sec_largest}")

# Check if List is sorted or not.
f = [1,2,3,4,5,6]
for i in range(len(f)-1):
    if f[i] < f[i+1]:
        continue
    else:
        print("your list in not sorted")
        break
else:
    print("your list is sorted")

# Tuple Powers
# Before starting we need to understand some of the terminology.

"""
Immutable - Tuples are not mutable you cannot change the values of tuple
Duplicate - You can have duplicate values in tuple there are no restriction
Ordered - Tuples are ordered and you can access them through index values
Heterogenous - Tuples also have heterogenous nature and can have different types of data structure in tuple.
"""

# Tuple Traversing and methods
"""
Tuples are traversed in the same manner as List are traversed
But remember tuples are like strings you can’t change anything once it’s made we can’t change them.
Well the use case is not much in question solving but still you
have to understand it
"""

# Methods of tuple are:

t = (1,2,4,2,5,2,1,3)

l = [1,5,4,6,2,7,8]
tup =tuple(l)
print(type(tup)) #<class 'tuple'>

index = t.index(2) # find index of first occurence of 2
print(index)
count_2 = t.count(2) # count occurence of 2 --> 3
print(count_2)

"""Yes there are only 2 methods of tuple one for finding them index and other of counting the occurrences of an element."""

# Tupple Unpacking
a,b,c,d = (1,3,5,7)
print(a,c,b,d)

def students():
    return "sandip", 23, "BCA"

info = students()
name, age, Department = info
print(name,age,Department)

# Sets -> A sets remove duplicate and has no guaranted order 

m = [1,4,4,1,5,5,2,1,2,3,3,5,4,5,7,6]
s = set(m)
print(s) # {1, 2, 3, 4, 5, 6, 7} it give the unique element

n = {10,20,30,40}
n.add(50) # {40, 10, 20, 30}
print(n) # {40, 10, 50, 20, 30} it is not in ordered so it can't be accessed with the help of index
n.discard(10) # Remove the specified element from the set
n.pop() # Remove the element from the set
print(n) 

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = {30,40}
print(s1-s2) ,# print(s1.difference(s2)) # {10,20}
# s1 -= s2
# print(s1)
print(s1 & s2) # print(s1.intersection(s2)) # {40,30}
# s1 &= s2
# print(s1)
print(s2 >= s3) # is s2 is a super set of s3 -> yes
print(s3 <= s2) # is s3 is a subset of s2 -> yes

print(s1^s2) # print(s1.symmetric_difference(s2)) # union - intersection {10, 50, 20, 60}
print(s1 | s2)  # print(s1.union(s2)) # {40, 10, 50, 20, 60, 30} all value

# Dictionaries: 
d = {10:11,20:200,30:300,40:400}
d[50] = 500 # creating a  new key value pair
print(d[30]) #Reading a value
d[10] = 100 # Updating a key value that already exists
print(d)

# Working with Dictionaries

employee = {
    "id": 101,
    "name": "Ravi",
    "salary": 50000
}
# Accessing Values
print(employee['name']) # Ravi
print(employee.get('salary')) # 50000

employee['city'] = "chirkunda" # Adding New Elements
employee['salary'] = 100000 # Updating Values
del employee['city'] # Deleting Elements
employee.pop('salary') # remove key value pair
employee.clear() # clear all the key value pair -> { }
print(employee)

# Dictionary Functions
student = {
    "name":"Sandip",
    "age":21,
    "city":"goa"
}
# len() - Returns number of items.

print(len(student)) # 2
print(type(student)) # <class 'dict'>

data = {
    1:"A",
    2:"B",
    3:"C"
}

print(max(data)) # 3
print(min(data)) # 1

# Dictionary Methods
# keys() - Returns all keys.
print(student.keys()) # dict_keys(['name', 'age', 'city'])
# values() - Returns all values.
print(student.values()) # dict_values(['Sandip', 21, 'goa'])
# items() - Returns key-value pairs.
print(student.items()) # dict_items([('name', 'Sandip'), ('age', 21), ('city', 'goa')])
# update() - Updates dictionary.
student.update({"city":"patna"}) 
# pop() - Removes specific key.
student.pop("age") # {'name': 'Sandip', 'city': 'patna'}
# popitem() - Removes last inserted item.
student.popitem() # {'name': 'Sandip'}
print(student)