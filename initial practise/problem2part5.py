'''Caesar Cipher
In Caesar cipher, each letter is replaced by another letter which occurs at the  d-th position (when counted from the position of the original letter),  in the  English alphabet.  For identifying the position of a letter, we follow the usual order of the English alphabet, from a to z. Given a word and a positive integer d, use Caesar cipher to encrypt it. For example, if the word is 'ball' and the value of 'd' is 3 then the new encrypted word is 'edoo'. 'x' will be replaced by 'a', 'y' should be replaced by 'b' and 'z' should be replaced by 'c'. While the code is submitted for Online Judge (SkillRack), use rstrip(), to remove carriage return character in the input.

Input Format

Word

A positive integer 'd'

Output format:

Encrypted word  '''



#Your code has Passed Execution!
word=input()
word.rstrip()
no=int(input())
no=abs(no)
no=no%26
t=[]
for i in range(len(word)):
    p=ord(word[i])+no
    if p>122:
        p=p-122
        p=96+p
        t.insert(i,chr(p))
    else:
        t.insert(i,chr(p))
for i in t:
    print(i,end='')














