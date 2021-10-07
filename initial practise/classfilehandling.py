'''f=open("file2.txt","w")
print("Name- ",f.name)
print("Closed??- ",f.closed)
print("Mode- ",f.mode)
f.close'''


'''f=open("file2.txt","w")
print("Name- ",f.name)
print("Closed??- ",f.closed)
print("Mode- ",f.mode)
f.write("Hello World!!")
f.close'''


'''f=open("D:\\file4.txt","w")
print("Name- ",f.name)
print("Closed??- ",f.closed)
print("Mode- ",f.mode)
f.write("Hello World!!")
f.close
f=open("D:\\file2.txt","r")
s=f.read()
print(s)'''


f=open("file4.txt","w")
print("Name- ",f.name)
print("Closed??- ",f.closed)
print("Mode- ",f.mode)
f.write("Hello World!!")
f.close
f=open("file4.txt","rb")
s=f.read()
print(s)
f.seek(-3,2)
print(f.read())
f.seek(2)
print(f.read())
f.seek(-3,1)
print(f.read())






























