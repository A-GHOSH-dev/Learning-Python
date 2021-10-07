'''l=['sfdsd','ASFSFS','cfgfDDgfjgh']

l.sort()

l
Out[3]: ['ASFSFS', 'cfgfDDgfjgh', 'sfdsd']

l=['sfdsd','ASFSFS','cfgfDDgfjgh']

l.sort(key=str.lower)

l
Out[6]: ['ASFSFS', 'cfgfDDgfjgh', 'sfdsd']

l.sort(key=str.lower,reverse=True)

l
Out[8]: ['sfdsd', 'cfgfDDgfjgh', 'ASFSFS']

l=[1,2]

l.extend([3,4,5])

l
Out[11]: [1, 2, 3, 4, 5]

l.pop(l[3])
Out[12]: 5

l.reverse()

l
Out[14]: [4, 3, 2, 1]

l.index(4)
Out[15]: 0

l.index(1)
Out[16]: 3

l.pop(1)
Out[17]: 3

l
Out[18]: [4, 2, 1]

l.count('4')
Out[19]: 0

del L[0]
Traceback (most recent call last):

  File "<ipython-input-20-2c74529004dc>", line 1, in <module>
    del L[0]

NameError: name 'L' is not defined


del l[0]

l
Out[22]: [2, 1]

del l[1:]

l
Out[24]: [2]

l1=[1,2,3,4,5,6]

del l[0:]

l
Out[27]: []

l1
Out[28]: [1, 2, 3, 4, 5, 6]

s='dgfddhdhrhbyyrersgf'

l=list(s)



l
Out[31]: 
['d',
 'g',
 'f',
 'd',
 'd',
 'h',
 'd',
 'h',
 'r',
 'h',
 'b',
 'y',
 'y',
 'r',
 'e',
 'r',
 's',
 'g',
 'f']

s='favourite'

l=list(s)

l
Out[34]: ['f', 'a', 'v', 'o', 'u', 'r', 'i', 't', 'e']

'SPAM'.join(['egg','gdsh','hgdssa'])
Out[35]: 'eggSPAMgdshSPAMhgdssa'             '''