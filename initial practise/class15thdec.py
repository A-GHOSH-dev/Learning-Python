#sets
#s4>s2 super set
#s1|s2 union
#s1&s2 intersection
#s2<s4 subset
#s.add(56) adds this element in 
#null set is represented by set()
#s1-s2
#s1.union(l1) or s1|set(l1)
'''s1.add(l1)
Traceback (most recent call last):

  File "<ipython-input-8-b528956de8a4>", line 1, in <module>
    s1.add(l1)

TypeError: unhashable type: 'list'


s1.add({1:"a",2:"b"})
Traceback (most recent call last):

  File "<ipython-input-9-b5447702e415>", line 1, in <module>
    s1.add({1:"a",2:"b"})

TypeError: unhashable type: 'dict'


s1.add((123,345,567))

s1
Out[11]: {(123, 345, 567), 1, 2, 3, 4, 5}'''


#s1=frozenset(["a","b","c"])   immutable

#1 in s1           #True or false
'''s1={1,2,3,4,5}
s2=s1.copy()
s2={1,2,3,4,5}   separate memory storage    is s2 had something else also, that will also stay'''

#s2.clear()
#s2=s3   storage in same memory location     so if i clear one of them, both will get cleared



'''s1={1,2,3,4,5}
s2={2,3,5,6}

s1-s2
Out[15]: {1, 4}

s1
Out[16]: {1, 2, 3, 4, 5}

s1.difference_update(s2)

s1
Out[18]: {1, 4}'''


#frozen set can be added to a set











