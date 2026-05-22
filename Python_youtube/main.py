print("namaste youtube we are learning python")
# comment in python'

# hello sandip it is single line comments

""" now me is baar
multi line comment ke bare me bata raha hu
dhyan rakho ye multiple line ko comment kar dega
bas karna ye hai ki 3 baar double quotes lagao or uske 
under sab likho - ise ham docs string bhi kahte hai """

# variable in python 
# In python variable is used as a storage to store things in python you can write anything as a variable name .
# variable banana bahut easy hota hai kuch bhi name likh do or unke baad equal to ka sign de do lekin iske under kisi chij ko store karna hoga.

name = "sandip saw"
a = 12 

#  there are three type of rule which are not used in variable
# 1. you cannot use number at variable start
# 1example = "nahi hai" ❌
# example1 = "sahi hai" ✅

# 2. you cannot use space in between variable or befor variable.
#  count = 10

# 3. you should not use special character in front of variable
# @example = "bgcxkj" ❌

# Naming Convention
# you can write variable in python using 3 way.
sheriyansSchool = "harsh Bhaiya" # camel case 
SheriyansSchool = "Harsh Bhaiya" # pascal case 
sheriyans_school = "Harsh Bhaiya" # snake Case -isme sab chota hoga bas underscore lagega
"""
What are Data Types

Data types are the things we store in Variables and it
defines what data type variables are.
Python has built-in data types for different kinds of data."""


# Numbers
# Integer- All the numbers excluding decimal places and fraction.
# Float- All the decimal numbers and fraction values are Float.
# Complex- Numbers with real and imaginary parts are complex.

"""Strings - This is used to store anything in python, literally anything
that are available on your keyboard.
You have to use quotes to store anything and it will be
considered as string. You can use double Quotes (“”) or
single quotes (‘’) to store both works same.

Boolean - Theres nothing much to say this is the data type which will and always give the result of True and False."""

"""
You know what strings are but you must also know stringtake more space than other data types like int, float etc
This happens because String stores every character with
their own Unicode
Unicode is a universal character encoding standard that
assigns a unique number (code point) to every character,
regardless of language
) Like “A” unicode is 65 and “😊” this emoji unicode is 128522,
and "🫶" this emoji unicode is 129782,you can check them by using ord() function in python and
convert them back using chr() function.
Unicode
"""

# print(ord('🫶')) --> 129782
# print(chr(129782)) --> 🫶

# String Indexing
"""You must have thought there are so many characters in a
string but can you access everyone.
Yes thats possible using indexing. Indexing starts from 0 and
goes till the number of characters you have.
There is negative indexing as well and it starts from -1, but
the starting position is from the back of the string
    [01234]
a = "Hello"
   -[54321] 
eg - a = “Hello” print(a[0]) ==> output - “H
eg - a = “Hello” print(a[-1]) ==> output - “o”
"""

# String Slicing

"""
You know how to access characters in string. But there are
slicing option as well.
Slicing means cutting out a slice from string and this is also
done using index values
So here we have start , stop and steps position and keep a
note if we use stop at 4 it will slice till 3 only.
eg - a = “hello” a[1:4:1] ==> output “ell:
here stop index is not selected as output
"""
# Type Conversion

"""
For understanding type conversion you have to look at these
4 things

int() float() str() bool()

There are more functions like this but these are 4 main
function, looking at these functions you can guess these are
used to convert one data type to another
eg a = 12
a = str(a)
print(a) ==> “12” (a will be converted to string)


Some important concepts of type conversions are you
cannot convert a character to a int() that basic watch the
video for more set of information

bool() converter turns everything to True and False but
which thing will be converted to true and which false. Lets
see.

 There are truthy values and Falsy values, and there are only
7 falsy values that means only 7 things will be converted to
false rest True.
0,0.0,false,"",[],{},()
All these values are falsy remaining will be converted to True.
"""

# name = input("Enter your name :-")
# age = input("Enter your age :-")
# print("your name is",name,"and your age is",age)
# print(f"your name is {name}! and your age is {age}")

# What are Operators
"""
Operators are symbols that perform operations on variables
and values. Python has several types of operators for
different tasks like arithmetic, comparison, logical operations,
and more
Lets see every operators one by one.
"""

# Arithmetic Operation

"""
Arithmetic operators perform mathematical operations like
addition, subtraction, multiplication, division, etc
 There are 7 types of arithmetic operator.G
 addition               +
 subtraction            -
 multiplication         *
 division               /
 Floor division         //
 modulus                %
 Exponentiation         **

"""
a = 15
b = 3
# print("Addition :",a+b)
# print("Multipliaction :",a*b)
# print("subtraction :",a-b)
# print("division :",a/b)
# print("floor division :",a//b)
# print("modulous :",a%b)
# print("exponential :",a**b)

# Assignment Operators:
"""
Assignment operators are used to assign values to variables.
Python also provides compound assignment operators that
perform operations like addition, subtraction, multiplication,
etc
 A basic assignment operator is simple =.
"""
# Compound assignment operator
"""
Compound assignment operator combines arithmetic
operations with assignment
 But first you have to understand how things work when we
reassign variables in python and also reassigning variables
with addition, subtraction etc
 To understand watch the video carefully
 Using compound assignment operators the reassigning
works better
 +=    Add and assig
 -=    Subtract and assig
 *=    Multiply and assign
 /=    Divide and assig
 //=   Floor divide and assig
 %=    modulus and assig
 **=   Exponentiation and assign
"""
# Comparison operator
"""
Comparison operators, also called relational operators, are
used to compare two values
Comparison operators will always provide Boolean result that
is True and False
comparison operators are as follow
==    Equal to
!=    Not Equal to
>     Greater than
<     Less than 
>=    Greater than or equal to
<=    Less than or equal to
Comparison operators will work with numbers but you can
use them with strings as well.
Strings will be comparing the Ascii values of string.
"""

# Logical operators

"""
Logical operators in Python are used to combine multiple
conditions and return a Boolean result (True or False)
There are 3 types of logical operator
and - Return True if both condition are True
or - Return True if at least one condition is True
not - Reverse the boolean value
**important** watch the full video for better understanding.
"""