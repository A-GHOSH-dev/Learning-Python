
'''CoPrime
Given two numbers ‘m’ and ‘n’, design an algorithm and write the Python code to check if they are relatively prime. Two integers ‘a’ and ‘b’ are said to be relatively prime, mutually prime, or coprime, if the only positive integer that divides both of them is 1. For example, 14 and 15 are coprime since the factors of 14 are 1, 2, 7, & 14 and factors of 15 are 1, 3, 5, & 15 and there is no common factor other than 1. (Use only conditional and iterational statements for designing the algorithm and implementation).

Input Format

Number m

Number n

Output Format

Print either Coprime or Not coprime'''

#Your code has Passed Execution!
m=int(input())
n=int(input())
from fractions import gcd
x=gcd(m,n)
if x==1:
    print('Coprime')
else:
    print('Not coprime')



#wrong mine code:
m=int(input())
n=int(input())
s1=set()
s2=set()
for i in range(1,m+1):
    if m%i==0:
        s1.add(i)
for j in range(1,n+1):
    if n%i==0:
        s2.add(j)
s3=s1&s2
if s3=={1}:
    print('Coprime')
else:
    print('Not coprime')










