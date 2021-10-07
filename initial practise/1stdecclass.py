'''
Dictionaries


d1={1:"aaa","b":1234,12.5:"abc","$a1":12.34}

d1
Out[5]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d1['$a1']
Out[6]: 12.34

d
Out[7]: {}

d[0]="ABCD"

d["vit"]="vellore"

d
Out[10]: {0: 'ABCD', 'vit': 'vellore'}

d[0]
Out[11]: 'ABCD'

d[0]="VIT"

d
Out[13]: {0: 'VIT', 'vit': 'vellore'}
d[1]="VIT"

d
Out[15]: {0: 'VIT', 'vit': 'vellore', 1: 'VIT'}
d
Out[17]: {0: 'VIT', 'vit': 'vellore', 1: 'VIT'}

del(d[0])

d
Out[19]: {'vit': 'vellore', 1: 'VIT'}

d.clear()

d
Out[21]: {}

d=d1

d
Out[23]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

len(d)
Out[24]: 4

d2=d1.copy()

d2
Out[26]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d=d

d=d1

d
Out[29]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}
l1=list(d.keys())

l1
Out[32]: [1, 'b', 12.5, '$a1']

l2=list(d.values())

l2
Out[34]: ['aaa', 1234, 'abc', 12.34]

l3=list(d.items())

l3
Out[36]: [(1, 'aaa'), ('b', 1234), (12.5, 'abc'), ('$a1', 12.34)]

d
Out[37]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d.get(1)
Out[38]: 'aaa'

d[1]
Out[39]: 'aaa'

d
Out[40]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d1
Out[41]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d2
Out[42]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d3={100:"A",200:"B"}

d=d.update(d3)

d

d

d=d1

d=d2

d1
Out[49]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34, 100: 'A', 200: 'B'}

d2
Out[50]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d
Out[51]: {1: 'aaa', 'b': 1234, 12.5: 'abc', '$a1': 12.34}

d=d.update(d3)

d



d.update(d3)
Traceback (most recent call last):

  File "<ipython-input-54-36ec497a43a8>", line 1, in <module>
    d.update(d3)

AttributeError: 'NoneType' object has no attribute 'update'


d3
Out[55]: {100: 'A', 200: 'B'}

d4={1:100,2:200,3:300}

d3[300]=d4

d3
Out[58]: {100: 'A', 200: 'B', 300: {1: 100, 2: 200, 3: 300}}

l1=[1,2,3,4]

d3[400]=l1

d3
Out[61]: {100: 'A', 200: 'B', 300: {1: 100, 2: 200, 3: 300}, 400: [1, 2, 3, 4]}

dict={x:x+2 for x in range(1,11)}

dict
Out[63]: {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11, 10: 12}

dict1={c:c*4 for c in 'SPAM'}

dict1
Out[65]: {'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}

dict2={a:ord(a) for a in "ANANYA"}

dict2
Out[67]: {'A': 65, 'N': 78, 'Y': 89}

print(str(dict1)
)
{'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}

s=str(dic1)
Traceback (most recent call last):

  File "<ipython-input-69-1147219f8084>", line 1, in <module>
    s=str(dic1)

NameError: name 'dic1' is not defined


s=str(dict)

s
Out[71]: '{1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11, 10: 12}'

s[0]
Out[72]: '{'

s[1]
Out[73]: '1'

s=str(dict1)

s
Out[75]: "{'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}"

s[0]
Out[76]: '{'

s[1]
Out[77]: "'"

s[2]
Out[78]: 'S'

s[3]
Out[79]: "'"

s[4]
Out[80]: ':'         '''
