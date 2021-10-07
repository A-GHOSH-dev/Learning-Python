amt=0

hour=int(input("Enter hours: "))

min=int(input("Enter minutes: "))

if hour>=5:
    amt=amt+200
    hour=hour-5
amt=amt+hour*50
amt=amt+min*1
print("the amount to be paid is ",amt)

amt=0

hour=int(input("Enter hours: "))

min=int(input("Enter minutes: "))

if hour>=5:
    amt=amt+200
    hour=hour-5
    print('Hello')
    
amt=amt+hour*50
amt=amt+min*1

print("the amount to be paid is ",amt)
