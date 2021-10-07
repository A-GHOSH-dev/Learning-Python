p=float(input("Enter phy marks: "))
if p<=0:
    print("invalid input")
    
c=float(input("Enter chem marks: "))
if c<=0:
    print("invalid input")
    
m=float(input("Enter maths marks: "))
if m<=0:
    print("invalid input")

else:
    total=p+c+m
    average=total/3 
    print (average)
  
    if average>=98:
         print("Candidate qualified for scholarship")
    else:
         print("camdidate not qualified for scholarship")