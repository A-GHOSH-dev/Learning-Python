'''n=int(input())
n1=1
count=0
while count<n+1:
    n2=1+(count/n1)
    n1=n2
    count+=1
print(n1)'''


'''4n=int(input())
def main():
    if (n>=1):
        f=1+n/1+(main(n-1))
        return main(f)
        print(f)'''

n=int(input())
x=1
i=0
for i in range(0,n+1):
    y=1+(i/x)
    x=y
    i=i+1
print(x)
