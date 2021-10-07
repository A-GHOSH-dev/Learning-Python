p=float(input("Enter phy marks: "))
c=float(input("Enter chem marks: "))
m=float(input("Enter maths marks: "))


if p<=0 or c<=0 or m<=0:
    print("invalid input")
  
else:
    total=p+c+m
    average=total/3 
    print ("The average is: ",average)
  
    if average>=98:
         print("Candidate qualified for scholarship")
    else:
         print("camdidate not qualified for scholarship")
    
#Enter phy marks: 96
#Enter chem marks: 95
#Enter maths marks: 98
#96.33333333333333
#camdidate not qualified for scholarship

#Enter phy marks: 0
#Enter chem marks: 90
#Enter maths marks: 98
#invalid input

#Enter phy marks: 100
#Enter chem marks: 98
#Enter maths marks: 100
#99.33333333333333
#Candidate qualified for scholarship

#Enter phy marks: 98
#Enter chem marks: 96
#Enter maths marks: 100
#The average is:  98.0
#Candidate qualified for scholarship