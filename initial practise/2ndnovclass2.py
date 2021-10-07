amt=0
hr=int(input())
min=int(input())
if hr>7:
    print('invalid')
elif 5<=hr<=7:
    amt=200+((hr-5)*50)+(min*1)
    print(amt)
elif 1<=hr<5:
    amt=hr*50+min*1
    print(amt)
elif hr<1:
    amt=min*1
    print(amt)
    
amt=0
h=int(input())
m=int(input())
if h<=7:
    amt=200+((h-5)*50)+(m*1)
    print(amt)
    