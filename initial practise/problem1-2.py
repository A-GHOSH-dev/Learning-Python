'''Digit Factors in a Number
Given a number ‘n’, design an algorithm and write the Python program to  print the digits of ‘n’ that  divides ‘n’. Print the digits in reverse order of their appearance in the number ‘n’.  For example, if n is 122 then print 2, 2, 1. Use only conditional and iterative statements to write the code. If none of the digits divide the number, then print ‘No factors’

Input Format

A number, n 

Output Format

Digits in the number ‘n’ that divides ‘n’ in reverse order'''

#Your code has Passed Execution!
n=int(input())
m=n
x=[]
for i in range(len(str(n))):
    d=n%10
    if m%d==0:
        x.append(d)
    n=n//10
for i in range(len(x)):
    print(x[i])
if len(x)==0:
    print('No factors')

















