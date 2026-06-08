"""import math

d1 = {"a":10,"b":20,"c":30}
d2 = {"d":40,"e":50,"f":60}

# combine both the dictionary

for i in d2:
    d1[i] = d2[i]

print(d1) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# sum of the value of dictionary

sum = 0
for i in d1:
    sum += d1[i]

print(f"sum={sum}") #210

s1 = {10,15,20,25}
s2 = {20,15,30,35}

# write the operation of the following function on a given set

union = s1.union(s2)
print(union)
intersection = s1.intersection(s2)
print(intersection)
difference = s1.difference(s2)
print(difference)

# write the operation of the following function on a given dictionary

d = {"a":10,"b":20,"c":30}
d.pop("b")
d.update({"a":15})
print(d.items())
print(d)

# write a program to find the lcm of two number using function

num1 = int(input("Enter first Number"))
num2 = int(input("Enter second Number")) 

def Lcm(a,b):
    return (a * b) // math.gcd(a,b)

print("lcm=",Lcm(num1,num2))

# write a program to find the gcd of two number using function

def gcd(a,b):
    while b!= 0:
        a, b = b, a%b
        print(a,b)
    return a

print("gcd = ",gcd(num1,num2))

# "Write a program in Python to find the sum of digits of any number."

num = int(input("Enter a number : "))
def sum_of_digit(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    return sum

print("sum=",sum_of_digit(num))

# "An email address is provided: hello@python.org. Using type assignment, split the username and domain from the email address."

email = "hello@pthon.org"
username , domain = email.split('@')
print("username:",username)
print("domain:",domain)
"""

# write a recursive function to find the factorial of number

num = 6
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)



number = int(input("Enter a number:"))

def Fact(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * Fact(n-1)


print("factorial:",Fact(number))

# write a function to display the factor of a given numbe

n = 148

lis = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transpose = []
for i in range(len(lis[0])):
    row = []
    for j in range(len(lis)):
        row.append(lis[j][i])
    transpose.append(row)

for row in transpose:
    print(row)

r = int(input("enter number of row"))
c = int(input("enter number of column"))

A = []
B = []
print("Enter elements of First Matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Second Matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Sum of Matrices:")
for row in result:
    print(row)