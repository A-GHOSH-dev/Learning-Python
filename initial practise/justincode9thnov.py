'''returndays=int(input('r'))
n=int(input('n'))
m=int(input('m'))
months=int(input('p'))
if months>12:
    fine=10000
    print(fine)
elif months<12:
    fine=(months-1)*500
    print(fine)
elif n>returndays and n<m:
    fine=(n-returndays)*15
    print(fine)
else:
    fine=0
    print(fine)
