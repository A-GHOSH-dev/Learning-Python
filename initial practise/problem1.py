'''Water in a Dam
A city has a dam of capacity ‘x’ litres, water comes to the dam from ‘n’ places.  Given the value of ‘n’ and the quantity of water (in litres and millilitres) that comes from ‘n’ places, Write an  algorithm and the corresponding Python code to determine the total amount of water in the dam. Assume that the total quantity of water in the dam, will be always less than the capacity of the dam. For example, if there are three places from which water comes to the dam and the water from place 1 is 2 litres 500 ml, water from second place is 3 litres 400 ml and water from third place is 1 litre 700 ml then the total quantity of water in dam will be 7 litres 600 ml.

Input Format

Number of places from where water comes, n

Number of litres of water from place-1

Number of millilitres of water from place-1

Number of litres of water from place-2

Number of millilitres of water from place-2

...

Number of litres of water from plac- n

Number of millilitres of water from place- n

Output Format

Total litres of water in the dam

Total millilitres of water in the dam'''



#Your code has Passed Execution!
a=int(input())
t1=0
tm1=0
for i in range(1,a+1):
    b=int(input())
    c=int(input())
    t1=t1+b
    tm1=tm1+c
tm1=str(tm1)
if len(tm1)>3:
    sum=t1+int(tm1[0])
    print(sum)
    print(tm1[-3]+tm1[-2]+tm1[-1])
else:
    print(t1)
    print(tm1)