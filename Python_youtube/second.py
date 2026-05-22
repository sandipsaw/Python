"""
money = int(input("enter the money:-"))

if money>10:
    print("i will do task A")
else:
    print("i will do task B")

"""

"""
sallary = int(input("Ener your salatry:-"))
if sallary>10000 and sallary<=20000:
    print("i buy a Cycle")
elif sallary>20000 and sallary<=50000:
    print("i buy a Eletric Cycle")
elif sallary>50000 and sallary<=200000:
    print("i buy a Motor-Cyle")
elif sallary>200000:
    print("i buy a 4 wheeler vechilce")
else:
    print("i dont buy anything")    
"""
# Accept two number and print greatest between them 
"""
a = int(input("Enter a first number:-"))
b = int(input("Enter a second number:-"))

if a>b:
    print(f"{a} is greater then {b}")
elif b>a:
    print(f"{b} is greater then {a}")
else:
    print("Both are the same number")
"""
# Accept the gender from the user as char and print the respective gretting message
"""
gender = input("Please enter your gender either M or F:-")
if gender == 'M' or gender == 'm':
    print("Good Morning Sir")
elif gender == 'F' or gender =='f':
    print("Good Morning maam")
else:
    print("You given wrong input")
"""

# Accept a integer and check wheater it is a even number or odd number
"""
number = int(input("Enter a number:-"))
if number%2 == 0:
    print(f"{number} is a even number")
else:
    print(f"{number} is a odd number")
"""

# Accept name and age from the user check if the user is valid voter or not
"""
name = input("Enter the name:-")
age = int(input("enter your age:-"))
if age < 18:
    print(f"hello {name} you are not a  valid voter")
else:
    print(f"hello {name} you are valid voter")
"""
# Accept a year and check if it is a leap year or not(google to find out what is a leap year)
"""
year = int(input("Enter a year:-"))

if year%4 == 0:
    if year%100 == 0:
        if year%400 ==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") 
"""

# You can also create if elif ladder using multiple conditions of elif.
"""
For understanding solve this questionj
take the input of temperature in celsius
Below 0°C → "Freezing Cold 🥶" 
0°C to 10°C → "Very Cold ❄️"
10°C to 20°C → "Cold 🧊"
20°C to 30°C → "Pleasant 🙂‍↔️"
30°C to 40°C → "Hot ♨️"
Above 40°C → "Very Hot 🥵"
"""

"""Solution---->
temp = int(input("Enter the temprature:-"))

if temp < 0:
    print("Freezing Cold 🥶")
elif temp > 0 and temp <= 10:
    print("Very Cold ❄️")
elif temp > 10 and temp <= 20:
    print("Cold 🧊")
elif temp > 20 and temp <= 30:
    print("Pleasant 🙂‍↔️")
elif temp > 30 and temp <= 40:
    print("Hot ♨️")
elif temp > 40:
    print("Very Hot 🥵")
else:
    print("un identified temprature")
"""

# For loop
# range(0,11,1) ---> range(start,stop,steps)

"""# print from 0,1,2...,10
for i in range(0,11,1):
    print(i)"""

"""# print from 15,16,17...35
for i in range(15,36,1):
    print(i)"""

"""# print from 10 to -5
for i in range(10,-6,-1):
    print(i)"""

"""# print from -5 to -20
for i in range(-5,-21,-1):
    print(i)"""

"""# print a odd number between 1 to 10
for i in range(1,11,2):
    print(i)"""

"""# print a table according to given input
num = int(input("Enter a number:-"))

for i in range(num,(num*10)+1,num):
    print(i)"""

# Loops for strings
s = "SHERIYANS TEACHES INDUSTRY THINGS"

"""for i in range(len(s)):
    print(s[i])"""

"""# another way to print the value of s one bye one
for i in s:
    print(i)"""

# Break and continues statement

"""for i in range(1,11,1):
    if i == 5:
        break
    else:
        print(i)
# ---> 1,2,3,4"""

"""for i in range(1,11,1):
    if i==5:
        continue
    else:
        print(i)
# --->1,2,3,4,6,7,8,9,10"""
    
# Accept an integer and print Hello world n times
n = int(input("enter a number:-"))

"""for i in  range(n):
    print('Hello world')"""

# Print natural number up to n
"""for i in range(1,n+1):
    print(i)"""

# Reverse for loop. Print n to 1
"""for i in range(n,0,-1):
    print(i)"""

# Take a number as input and print its table
"""for i in range(n,(n*10)+1,n):
    print(i)"""

# Sum up to n terms
"""sum = 0
for i in range(1,n+1):
    sum += i
print(sum)"""

# Factorial of a number
"""fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)"""

# Print the sum of all even & odd numbers in a range separately

"""sum_odd = 0
sum_Even = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum_Even += i
    else:
        sum_odd += i
print("sum of even number:",sum_Even)
print("sum of odd number:",sum_odd)"""

# Print all the factors of a number
"""for i in range(1,(n//2)+1,1):
    if n % i == 0:
        print(i)"""

# Accept a number and check if it a perfect number or not.
