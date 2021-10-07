password = input()
length = len(password)
count_digit = 0
count_special = 0
if length >= 8:
    for i in range(length):
        if i == 0:
            if password[0].isalpha() == False:
                break
        else:
            if password[i].isdigit() == True:
                count_digit+=1
                continue
            elif password[i].isalpha() == False:
                count_special+=1
                continue
if count_digit == 0 or count_special == 0:
    print('Invalid')
else:
    print('Valid')
    
    
    
    
''' Password Check
Given a word, check if it is a valid password or not.  A password is said to be valid if it satisfies the following conditions:

i) Should begin with a letter

ii) Should contain atleast one digit and one special character

iii) Length of the password should be atleast 8

Print ‘Valid' if the given word satisfies the above three conditions  and print ‘Invalid’ otherwise.

Input format:

A word

Output format:

Print ‘Valid' if the given word satisfies the above three conditions  and print ‘Invalid’ otherwise.'''



word=input()
word=list(word)
numbers = sum(c.isdigit() for c in word) #number of digits
words   = sum(c.isalpha() for c in word) #number of words
spaces  = sum(c.isspace() for c in word) #number of spaces
others  = len(word) - numbers - words - spaces #number of special characters
flag=0 #assume
if(len(word)>=8):
    if(word[0].isalpha()):
        if(numbers>0):
            if(others>0):
                flag=1
if(flag==1):
    print('Valid')
else:
    print('Invalid');   



























