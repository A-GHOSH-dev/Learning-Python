''' tup1=('physics','chemistry',1997,2000)

tup2=(1,2,3,4,5)

tup3="a","b","c","d","e"

print("tup1[0]:",tup1[0])
tup1[0]: physics

print("tup2[1:5]:",tup2[1:5])
tup2[1:5]: (2, 3, 4, 5)

(1,2)+(3,4)
Out[7]: (1, 2, 3, 4)

(1,2)*4
Out[8]: (1, 2, 1, 2, 1, 2, 1, 2)

T=(1,2,3,4)

T[0].T[1:3]
Traceback (most recent call last):

  File "<ipython-input-10-e3c52903108f>", line 1, in <module>
    T[0].T[1:3]

AttributeError: 'int' object has no attribute 'T'


T[0],T[1:3]
Out[11]: (1, (2, 3))

t1=(1,2,3,4)

t1=(3,1,4,2,5,9,6)

sorted(t1)
Out[14]: [1, 2, 3, 4, 5, 6, 9]

l1=sorted(t1)

l1
Out[16]: [1, 2, 3, 4, 5, 6, 9]

l[0]=10
Traceback (most recent call last):

  File "<ipython-input-17-10447767d9fb>", line 1, in <module>
    l[0]=10

NameError: name 'l' is not defined


t1[0]
Out[18]: 3

l1[0]=10

l1
Out[20]: [10, 2, 3, 4, 5, 6, 9]

t1[0]=10
Traceback (most recent call last):

  File "<ipython-input-21-c7bad9d4135c>", line 1, in <module>
    t1[0]=10

TypeError: 'tuple' object does not support item assignment


t2=l1

t2
Out[23]: [10, 2, 3, 4, 5, 6, 9]

t2[0]=20

t2
Out[25]: [20, 2, 3, 4, 5, 6, 9]

t2=tuple(l1)

t2
Out[27]: (20, 2, 3, 4, 5, 6, 9)

t2[0]=30
Traceback (most recent call last):

  File "<ipython-input-28-b957f17cde05>", line 1, in <module>
    t2[0]=30

TypeError: 'tuple' object does not support item assignment


T=(1,2,3,4,5)

L=[x+20 for x in T]

L
Out[31]: [21, 22, 23, 24, 25]



T1=(1,2,3,2,4,2)

t1
Out[33]: (3, 1, 4, 2, 5, 9, 6)

del(t1)

t1
Traceback (most recent call last):

  File "<ipython-input-35-5db19043943a>", line 1, in <module>
    t1

NameError: name 't1' is not defined


T.append(T1)
Traceback (most recent call last):

  File "<ipython-input-36-3433f6cbc459>", line 1, in <module>
    T.append(T1)

AttributeError: 'tuple' object has no attribute 'append'


t2
Out[37]: (20, 2, 3, 4, 5, 6, 9)

t2=t2+(45,56,67,78)

t2
Out[39]: (20, 2, 3, 4, 5, 6, 9, 45, 56, 67, 78)

t2.index(45)
Out[40]: 7

t2.index(67,4)
Out[41]: 9

t2.index(67,4)
Out[42]: 9

t2(67)
Traceback (most recent call last):

  File "<ipython-input-43-b93730f0b699>", line 1, in <module>
    t2(67)

TypeError: 'tuple' object is not callable


t2.index(67)
Out[44]: 9

t2.count(45)
Out[45]: 1

t2
Out[46]: (20, 2, 3, 4, 5, 6, 9, 45, 56, 67, 78)

t3=(1,2,2,2,3,5,6,7,7)

t3.count(2)
Out[48]: 3

t3
Out[51]: (1, 2, 3, 4, 5, 6, 3, 4, 2)

t3+(8,9,10,11,12)
Out[52]: (1, 2, 3, 4, 5, 6, 3, 4, 2, 8, 9, 10, 11, 12)

t4=(1,"aaaa",9.8,[1,2,3,4])

t4[0]
Out[54]: 1



t4[3]
Out[55]: [1, 2, 3, 4]

l1=[20,30,40]

t4[3]=l1
Traceback (most recent call last):

  File "<ipython-input-57-ee32a7d7c6ac>", line 1, in <module>
    t4[3]=l1

TypeError: 'tuple' object does not support item assignment


t4[3][0]
Out[58]: 1

t4[3][0]=20

t4[3][1]=30

t4[3][2]=40

t4[3]
Out[62]: [20, 30, 40, 4]


d1={1:"aaa",2:"bbb",3:"ccc"}

t1=tuple(d1.keys())

t1
Out[65]: (1, 2, 3)

l1=list(d1.keys())

l1
Out[67]: [1, 2, 3]

t1
Out[68]: (1, 2, 3)

t2
Out[69]: (20, 2, 3, 4, 5, 6, 9, 45, 56, 67, 78)

t1,t2
Out[70]: ((1, 2, 3), (20, 2, 3, 4, 5, 6, 9, 45, 56, 67, 78))

max(t1)
Out[71]: 3

min(t1)
Out[72]: 1





l1=[(20,30),(35.5,40),(12,15),(120,150),(80,120)]

v1=int(input())

25

if (v1>l1[0][0]) and (v1<l1[0][1]):
    print('Normal')
else:
    print('Abnormal')

Normal'''





