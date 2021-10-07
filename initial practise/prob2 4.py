'''Distinct Letter
A word is called as a good word if all the letters of the word are distinct. That is, all the letters of the word are different from each other letter. Else, the word is called as a bad word.

Write an algorithm and the subsequent Python code to check if the given word is good or bad.: e.g. START, GOOD, BETTER are bad: WRONG is good! Make the comparison to be case insensitive.

Input format:

A word

Output format:

Print ‘Good’ if all letters of the word are distinct and print ‘bad’ otherwise'''



word=input().lower()
l=list(word)
count=0
for i in range(len(l)):
    count=count+l.count(l[i])
if(count==len(l)):
    print('Good')
else:
    print('Bad')

















