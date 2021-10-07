'''n=int(input())
if n>0:
    x=1
    while(x<=n):
        y=1
        while(y<=x):
            print('*',end='')
            y+=1
        print()
        x+=1
else:
    print("invalid input")'''




'''for i in range(1,5):
    print(str(i)+'\n')
    for j in range(i,i+1):
        print(j,end=" ")'''


n=int(input())
if n>0:
    x=1
    while(x<=n):
        y=1
        while(y<=x):
            for i in range(1,5):
                print(str(i)+'\n')
                for j in range(i,i+1):
                    print(j,end=" ")


'''n=int(input())
if n>0:
    x=1
    while(x<=n):
        y=1
        while(y<=x):
            print('*',end='')
            y+=1
        print()
        x+=1
else:
    print("invalid input")'''























'''
1
1 2
1 2 3
1 2 3 4

1
2 3
4 5 6
7 8 9 10



4
4 3
4 3 2
4 3 2 1


1
2 1
3 2 1
4 3 2 1'''
