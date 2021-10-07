

'''def remove_stopwords(s):
    words=s.split()
    l1=['a','an','the','this','that','is','are','was','were','and','in']
    for word in words:
        w=word.lower()
        if w in l1:
            words.remove(word)
    return words
    return remove_stopwords()
s=input()
words=remove_stopwords(s)
#print(words)

def ismagic(words):
    for i in words:
        for j in range(0,len(i)):
            
            p=list(i[j])
            n=len(p)
        print(p)
        for k in range(0,n//2,1):
            if (k%2==0):
                if p[k]>p[n-1-k]:
                    p.remove(p[k])
            else:
                if p[k]<p[n-1-k]:
                    p.remove(p[n-k-1])
        j=''.join(p)
    return j
    return ismagic()

j=ismagic(words)
print(j)'''v





'''s=input().split()
stop_words=['a','an','and','the','this','is','in','was','that','this','are','were']
#pre-processing
#removing stop words
for i in stop_words:
    for j in s:
        if j==i:
            s.remove(j)

#if it is magic word or not
def magic_word(s):
    
    for i in s:
        if i.islower()==True:
            for j in range((len(s)//2)+1):
                if j%2==0:
                    if ord(s[j])<ord(s[len(s)-1-j]):
                        cond2=True
                        if (cond1 and cond2)==True:
                            return True
check=magic_word(s)
#2.magic word
if check==False:
    for j in range((len(s)//2)+1):
        if j%2==0:
            if ord(s[j])<ord(s[len(s)-j-1]):
                cond1=True
            else:
                s.remove(s[len(s)-1-j])
        if j%2!=0:
            if ord(s[j])>ord(s[len(s)-1-j]):
                cond2=True
            else:
                s.remove(s[j])'''


def check_magic(y:str):
    n=len(y)
    i=0
    index_to_rem=[]
    while i<=((n//2)) and n>1:
        if i%2==0:
            if hash[y[i]]<=hash[y[n-1-i]]:i+=1
            else:
                y=list(y)
                del y[i]
                y="".join(y)
                n=len(y)
                i=0
        else:
            if hash[y[i]]>=hash[y[n-1-i]]:i+=1
            else:
                y=list(y)
                del y[n-i-1]
                y="".join(y)
                n=len(y)
                i=0
    y=list(y)
    for x in sorted(index_to_rem,reverse=True):del y[x]
    return "".join(y)

letters="abcdefghijklmnopqrstuvwxyz"
hash={x:letters.index(x) for x in letters}
sentence=input().split()
stopwords=['a','an','the','this','that','is','are','was','were','and','in']
for x in sentence:
    if x in stopwords:sentence.remove(x)
new_li=[]
for y in sentence:
    res=check_magic(y)
    new_li.append(res)
n=min([len(k) for k in new_li])
arr=[[p[i] for i in range(0,n)] for p in new_li]
m=len(arr)

#rotating by 90 degree
for i in range(0,n//2):
    for j in range(0,n-1):
        temp=arr[i][j]
        arr[i][j]=arr[j][n-i-1]
        arr[j][n-1-i]=arr[n-i-1][n-j-1]
        arr[n-i-1][n-j-1]=arr[n-j-1][i]
        arr[n-j-1][i]=temp

#rotating left by one element(_p,_q,_r,_s counters)
temp=arr[0][0]
for _p in range(0,n-1):
    arr[0][_p]=arr[0][_p+1]
arr[0][n-1]=arr[1][n-1]
for _q in range(1,m-1):
    arr[_q][n-1]=arr[_q+1][n-1]
arr[m-1][n-1]=arr[m-1][n-2]
for _r in range(n-2,0,-1):
    arr[m-1][_r]=arr[m-1][_r-1]
arr[m-1][0]=arr[m-2][0]
for _s in range(m-2,0,-1):
    arr[_s][0]=arr[_s-1][0]
arr[1][0]=temp

for x in arr:
    for i in range(n):
        print(x[i],end=' ')
    print()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                   



























