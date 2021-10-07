'''s1=(1,2,3,4,3,2,1,5,6,5,6,4,7)

In [2]: s1
Out[2]: (1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 6, 4, 7)

In [3]: s1[2]=8
Traceback (most recent call last):

  File "<ipython-input-3-22cad3d7a594>", line 1, in <module>
    s1[2]=8

TypeError: 'tuple' object does not support item assignment


In [4]: s1.count(4)
Out[4]: 2

In [5]: t1=tuple(s1)

In [6]: t1
Out[6]: (1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 6, 4, 7)

In [7]: t1.count(4)
Out[7]: 2

In [8]: t1.index(3)
Out[8]: 2'''


'''def printer(m):
    print(m)
i=int(input())
printer(i)
f=float(input())
printer(f)
str=input()
printer(str)
l1=[10,20,30]
printer(l1)
d1={1:"AAAA",2:"BBBB",3:"CCCC"}
printer(d1)'''


'''def adder(a,b=1,*c):
    return a+b+c[0]'''


'''def sqr(n):
    res=n*n
    return res
num=int(input())
print(sqr(num))'''



'''def intersect(seq1,seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res'''


'''a=4
if a%2==0:
    def func():
        print('even')
else:
    def func():
        print('odd')
func()


output: even'''


'''def one():
    print('one')
def two():
    print('two')
def three():
    print('three')

a=3
if a==1:
    call_Func=one
elif a==2:
    call_Func=two
elif a==3:
    call_Func=three
call_Func()'''



'''x=100
l=[1,2,3,4]
def func(y):
    x=1000
    z=x+y
    print(z)
val=int(input())
func(val)
print("x= ",x)'''
















































































































