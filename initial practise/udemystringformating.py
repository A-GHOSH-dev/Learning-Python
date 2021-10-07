'''for i in range(1,13):
    print('No. {0} square is {1} cubed is {2}\n'.format(i,i**2,i**3))'''
    
    
'''No. 1 square is 1 cubed is 1

No. 2 square is 4 cubed is 8

No. 3 square is 9 cubed is 27

No. 4 square is 16 cubed is 64

No. 5 square is 25 cubed is 125

No. 6 square is 36 cubed is 216

No. 7 square is 49 cubed is 343

No. 8 square is 64 cubed is 512

No. 9 square is 81 cubed is 729

No. 10 square is 100 cubed is 1000

No. 11 square is 121 cubed is 1331

No. 12 square is 144 cubed is 1728'''
    
    
    
'''for i in range(1,13):
    print('No. {0:2} square is {1:4} cubed is {2:4}\n'.format(i,i**2,i**3))'''
    
    
'''No.  1 square is    1 cubed is    1

No.  2 square is    4 cubed is    8

No.  3 square is    9 cubed is   27

No.  4 square is   16 cubed is   64

No.  5 square is   25 cubed is  125

No.  6 square is   36 cubed is  216

No.  7 square is   49 cubed is  343

No.  8 square is   64 cubed is  512

No.  9 square is   81 cubed is  729

No. 10 square is  100 cubed is 1000

No. 11 square is  121 cubed is 1331

No. 12 square is  144 cubed is 1728'''



'''for i in range(1,13):
    print('No. {0:8} square is {1:2} cubed is {2:2}\n'.format(i,i**2,i**3))'''
    
    
'''No.        1 square is  1 cubed is  1

No.        2 square is  4 cubed is  8

No.        3 square is  9 cubed is 27

No.        4 square is 16 cubed is 64

No.        5 square is 25 cubed is 125

No.        6 square is 36 cubed is 216

No.        7 square is 49 cubed is 343

No.        8 square is 64 cubed is 512

No.        9 square is 81 cubed is 729

No.       10 square is 100 cubed is 1000

No.       11 square is 121 cubed is 1331

No.       12 square is 144 cubed is 1728'''

# the :2, :8, :4, are given, are given as space

'''for i in range(1,13):
    print('No. {0:2} square is {1:3} cubed is {2:4}\n'.format(i,i**2,i**3))

for i in range(1,13):
    print('No. {0:2} square is {1:<3} cubed is {2:<4}\n'.format(i,i**2,i**3))'''

#left align with < sign
'''No.  1 square is   1 cubed is    1

No.  2 square is   4 cubed is    8

No.  3 square is   9 cubed is   27

No.  4 square is  16 cubed is   64

No.  5 square is  25 cubed is  125

No.  6 square is  36 cubed is  216

No.  7 square is  49 cubed is  343

No.  8 square is  64 cubed is  512

No.  9 square is  81 cubed is  729

No. 10 square is 100 cubed is 1000

No. 11 square is 121 cubed is 1331

No. 12 square is 144 cubed is 1728

No.  1 square is 1   cubed is 1   

No.  2 square is 4   cubed is 8   

No.  3 square is 9   cubed is 27  

No.  4 square is 16  cubed is 64  

No.  5 square is 25  cubed is 125 

No.  6 square is 36  cubed is 216 

No.  7 square is 49  cubed is 343 

No.  8 square is 64  cubed is 512 

No.  9 square is 81  cubed is 729 

No. 10 square is 100 cubed is 1000

No. 11 square is 121 cubed is 1331

No. 12 square is 144 cubed is 1728'''


# for centering use ^




'''print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))'''


'''Pi is approximately 3.142857142857143
Pi is approximately     3.142857
Pi is approximately 3.14285714285714279370154144999105483293533325195312
Pi is approximately 3.14285714285714279370154144999105483293533325195312
Pi is approximately           3.14285714285714279370154144999105483293533325195312
Pi is approximately 3.14285714285714279370154144999105483293533325195312                    
Pi is approximately 3.142857142857142793701541449991054832935333251953125000 '''               

'''for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

No. 1 squared is 1 and cubed is    1
No. 2 squared is 4 and cubed is    8
No. 3 squared is 9 and cubed is   27
No. 4 squared is 16 and cubed is   64
No. 5 squared is 25 and cubed is  125
No. 6 squared is 36 and cubed is  216
No. 7 squared is 49 and cubed is  343
No. 8 squared is 64 and cubed is  512
No. 9 squared is 81 and cubed is  729
No. 10 squared is 100 and cubed is 1000
No. 11 squared is 121 and cubed is 1331
No. 12 squared is 144 and cubed is 1728'''

#f-string

'''greeting='hello, everyone, I am Titli'
print(type(greeting))
age=466345
print(type(age))

<class 'str'>
<class 'int'>'''


'''name='Tom'
age=24
print(name+f" is {age} years old")

Tom is 24 years old'''

'''print(f"Pi is approximately {22/7:12.50f}")

Pi is approximately 3.14285714285714279370154144999105483293533325195312'''

#meal4='''jhdkhs
#jgksegf
#tfasfgdas
#print(meal4) #jhdkhs
              #jgksegf
              #tfasfgdas

#meal3="""hdsfvahsfk
#vhjcvasghA
#ghdacs"""
#print(meal3)
#hdsfvahsfk
#vhjcvasghA
#ghdacs

#print('ananya\tchanna\tpadma') ananya	channa	padma


















































































































































































































