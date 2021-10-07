'''word=input('Enter the word: ')
n=len(word)
code=""
for i in range(0,n):
    if (word[i]=='x'):
        code=code+'a'
    elif (word[i]=='y'):
        code=code+'b'
    elif (word[i]=='z'):
        code=code+'c'
    else:
        code=code+chr(ord(word[i])+3)
print(code)'''

'''for i in range(0,n):
    code=code+chr((ord(word[i])-97+3)%26+97)
print(code)



for i in range(0,n):
    if (ord(word[i])>64 and ord(word[i])<91):
        op=op+chr(ord(ip[i])-65+3)%26+65)
    elif(ord(ip[]))
    code=code+chr((ord(word[i])-97+3)%26+97)
print(code)'''



key="fivejugs"
map1="abcdefghijklmnopqrstuvwxyz"
map2="fivejugsabcdhklmnopqrtwxyz"
ip=input("Enter the string: ")
n=len(ip)
op=""
for i in range(0,n):
    op=op+map2[(ord(ip[i])-97)]
print(op)
    




























