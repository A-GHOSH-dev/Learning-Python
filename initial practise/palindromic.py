#Palindrome Program
#1.
str = 'MaDaM'  
strstr = str.casefold()   
rev = reversed(str)  
if list(str) == list(rev):  
   print("PALINDROME")  
else:  
   print("NOT PALINDROME")  

#2.
string=input(("Enter a word:"))  
if(string==string[::-1]):  
      print("The word is a palindrome")  
else:  
      print("The word is not a palindrome")

#3.
num = int(input("Enter a value:"))  
num1 = num 
r = 0  
while(num1 > 0):  
    d = num1 % 10  
    r = r * 10 + d  
    num1 = num1 // 10  
if(num == r):  
    print(num,"This value is a palindrome number!")  
else:  
    print(num,"This value is not a palindrome number!")
    
    
    
    
    
    
    