'''a=int(input())
b=int(input())
c=int(input())
if (a==b) and (a==c):
    print('All are equal')
if a>b and a>c:
    print(a,'is greatest')
elif b>a and b>c:
    print(b,'is greatest')
elif c>a and c>b:
    print(c,'is greatest')
if (a==b) and (a>c or a<c):
    print('{0} is equal to {1}'.format(a,b))
elif (a==c) and (a>b or a<b):
    print('{0} is equal to {1}'.format(a,c))
elif (b==c) and (b>a or b<a):
    print('{0} is equal to {1}'.format(b,c))



a=int(input('The first number is '))
b=int(input('The second number is '))
c=int(input('The third number is '))
if (a==b) and (a==c):
    print('\nAll are equal')
if a>b and a>c:
    print('\n'+str(a),'is greatest')
elif b>a and b>c:
    print('\n'+str(b),'is greatest')
elif c>a and c>b:
    print('\n'+str(c),'is greatest')
if (a==b) and (a>c or a<c):
    print('\nThe first and second inputs are equal and the value is',a)
    if a>c:
        print('\n'+str(a),'is greatest')
    elif a<c:
        print('\n'+str(c),'is greatest')
elif (a==c) and (a>b or a<b):
    print('\nThe first and third inputs are equal and the value is',a)
    if a>b:
        print('\n'+str(a),'is greatest')
    elif a<b:
        print('\n'+str(b),'is greatest')
elif (b==c) and (b>a or b<a):
    print('\nThe second and the third inputs are equal and the value is',b)
    if b>a:
        print('\n'+str(b),'is greatest')
    elif b<a:
        print('\n'+str(a),'is greatest')
    



a=int(input('The first number is '))
b=int(input('The second number is '))
c=int(input('The third number is '))
if (a==b) and (a==c):
    print('\nAll are equal')
if (a==b) and (a>c or a<c):
    print('\nThe first and second inputs are equal and the value is',a)
    if a>c:
        print('\n'+str(a),'is greatest')
    elif a<c:
        print('\n'+str(c),'is greatest')
elif (a==c) and (a>b or a<b):
    print('\nThe first and third inputs are equal and the value is',a)
    if a>b:
        print('\n'+str(a),'is greatest')
    elif a<b:
        print('\n'+str(b),'is greatest')
elif (b==c) and (b>a or b<a):
    print('\nThe second and the third inputs are equal and the value is',b)
    if b>a:
        print('\n'+str(b),'is greatest')
    elif b<a:
        print('\n'+str(a),'is greatest')
elif a!=b and a!=c:
    if a>b and a>c:
        print('\n'+str(a),'is greatest')
    elif b>a and b>c:
        print('\n'+str(b),'is greatest')
    elif c>a and c>b:
        print('\n'+str(c),'is greatest')
        
    
    
    
    
    
    
x=True

y=10

z=20

a=y if x else z

a
Out[64]: 10

x=False

a=y if x else z

a
Out[67]: 20




n=int(input())
total=0
i=1
while i<=n:
    i=i+1
    mark=int(input())
    total=total+mark
avg=total/n
print("\nThe class average is",format(avg,'.2f'))'''


'''n=int(input())
total=0
i=0
while i<n:
    i=i+1
    mark=int(input())
    total=total+mark
avg=total/n
print("\nThe class average is",format(avg,'.2f'))


st=int(input())
en=int(input())
i=st
while i<=en:
    print(i,end=' ')
    i+=1'''#horizontal with space


'''st=int(input())
en=int(input())
i=st
while i<=en:
    print(i)
    i+=1'''#vertical



'''while True:
    name=input('Enter Name: ')
    if name=='stop':break
    age=int(input('Enter Age: '))
    print('\nHello',name,'=>',age**2)
    
 
#Enter Name: Ananya

#Enter Age: 17

#Hello Ananya => 289

#Enter Name: stop

x=100
while x:
    x=x-1
    if x%2!=0:continue
    print(x,end=' ')'''
    




y=int(input())
if y==0:
    print('Zero is neither prime nor composite')
elif y<0:
    print('Prime numbers check can be done only for positive numbers')
else:
    x=y//2
    while x>1:
        if x%y==0:
            print('Not a prime')
            break
        x-=1
    else:
            print('It is prime')
    print("end of if else")
print('end of program')