'''Pattern
Given ‘n’, the number of rows, design an algorithm and write a Python code to draw a pattern. If n is ‘5’, the pattern looks as shown below:

**

****

******

********

**********           '''



#Your code has Passed Execution!
n=int(input())
for i in range(1,n+1):
    j=2*i
    print('*'*j)