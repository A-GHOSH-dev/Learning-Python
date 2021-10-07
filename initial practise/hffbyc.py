'''def paper(text):
    result=""
    for i in text:
        result=result+i*3
    return result
answer=paper("Mississippi")
print(answer)'''



'''n=(input())
arr=list(n)
def find(arr):
    
    return '007' in ''.join(str(i) for i in arr)

    return find
    print(find(arr))//'''
    
    
    
def number(num):
    delta = [0,0,7, 'x']
    for x in num:
        if x == delta[0]:
            delta.pop(0)
    return len(delta) == 1

print(number([5,0,5,0,7]))


