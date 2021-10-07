'''l=[1,2,4,7,6,9,8,5,0]
l.append(78)

l
Out[4]: [1, 2, 4, 7, 6, 9, 8, 5, 0, 78]

l.insert(5,200)

l
Out[6]: [1, 2, 4, 7, 6, 200, 9, 8, 5, 0, 78]

l.index(6)
Out[7]: 4

l.insert(-5,300)

l
Out[9]: [1, 2, 4, 7, 6, 200, 300, 9, 8, 5, 0, 78]
l.pop(6)
Out[11]: 300

l.pop()
Out[12]: 78

l.pop(67)
Traceback (most recent call last):

  File "<ipython-input-13-3c2b87a280af>", line 1, in <module>
    l.pop(67)

IndexError: pop index out of range


l.remove(7)

l
Out[15]: [1, 2, 4, 6, 200, 9, 8, 5, 0]
l.reverse()

l
Out[19]: [0, 5, 8, 9, 200, 6, 4, 2, 1]

l1=['vit','100']

l.append(l1)

l
Out[22]: [0, 5, 8, 9, 200, 6, 4, 2, 1, ['vit', '100']]

l.reverse()

l
Out[24]: [['vit', '100'], 1, 2, 4, 6, 200, 9, 8, 5, 0]

l[0]
Out[25]: ['vit', '100']

l[0][0]
Out[26]: 'vit'

l.sort()
Traceback (most recent call last):

  File "<ipython-input-27-fb07ac7c73ab>", line 1, in <module>
    l.sort()

TypeError: '<' not supported between instances of 'int' and 'list'


l
Out[28]: [['vit', '100'], 1, 2, 4, 6, 200, 9, 8, 5, 0]

l.pop(0)
Out[29]: ['vit', '100']

l.sort()

l
Out[31]: [0, 1, 2, 4, 5, 6, 8, 9, 200]
l.sort(reverse=True)

l
Out[33]: [200, 9, 8, 6, 5, 4, 2, 1, 0]



 matrices
 
m=[[[]for i in range(0,3)] for i in range(0,3)]

m
Out[52]: [[[], [], []], [[], [], []], [[], [], []]]

m[0][0]=1

m[0][1]=2

m[0][2]=3

m
Out[56]: [[1, 2, 3], [[], [], []], [[], [], []]]'''



