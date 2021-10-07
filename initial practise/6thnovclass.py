'''while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    ch=int(input())
    if ch==5:
        break
    elif ch>5 or ch<1:
        print('invalid choice...')
    else:
        x=int(input("enter first value"))
        y=int(input("enter second value"))
        if ch==1:
            z=x+y
        elif ch==2:
            z=x-y
        elif ch==3:
            z=x*y
        elif ch==4:
            z=x/y
            print('the result is',z)'''




'''cnt=0
tot=0
n=int(input("Enter the number of students"))
while cnt<n:
    mark=int(input("Enter mark:"))
    if mark<0:
        print('INVALID INPUT')
        break
    tot=tot+mark
    cnt+=1
else:
    avg=tot/n
    print("Class average is:",avg)
print("End of the program")'''




'''n=int(input())
if n>0:
    x=1
    while(x<=n):
        y=1
        while(y<=x):
            print('*',end='')
            y+=1
        print()
        x+=1
else:
    print("invalid input")'''
 
#10
'''*
**
***
****
*****
******
*******
********
*********
**********''' 


'''n=int(input())
if n>0:
    x=1
    while(x<=n):
        print('#'*x)
        x+=1
else:
    print("invalid input")'''




print('enter the number of steps')
n=int(input())
for i in range(0,n):
    for j in range(1,n+1):
        print('#',end=' ')
    print()
    
       
           