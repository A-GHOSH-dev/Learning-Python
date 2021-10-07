n=int(input())
for i in range(2,n//2):
    if n%i==0:
        print("The number entered is Not prime");
    break
    else:
        print("The number entered is prime")