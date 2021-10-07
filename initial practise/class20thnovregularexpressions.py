import re
str=input("Enter a string:")
if (re.match('^[a-z]*[a.b]$',str)):
    print("Match found")
else:
    print("Match not found")






