'''n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("#",end=' ')
    print()'''

import time 
  
n = 5
  
'''print("----------Right Angled Triangle Type 1----------") 
  
def right_angle_triangle1(n): 
      
    for i in range(1, n + 1): 
        for j in range(i): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
       
right_angle_triangle1(n) 
  
print() '''


print("----------Right Angled Triangle Type 2----------") 
  
def right_angle_triangle2(n): 
      
    for i in range(1, n + 1): 
        for j in range(n-i): 
            time.sleep(0.05) 
            print(" ", end ="") 
        for k in range(i): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
right_angle_triangle2(n) 
  
print() 
  
print("----------Equilateral Triangle----------") 
  
def equilateral_triangle(n): 
      
    for i in range(1, n + 1): 
        for j in range(n-i): 
            time.sleep(0.05) 
            print(" ", end ="") 
        for k in range(2 * i-1): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
equilateral_triangle(n) 
  
print() 
  
print("----------Square----------") 
  
def square(n): 
      
    for i in range(1, n + 1): 
        for j in range(1, n + 1): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
square(n) 
  
print() 
  
print("----------Diamond----------") 
  
def diamond(n): 
      
    cell = n//2 + 1
    for i in range(1, cell + 1):  
        for j in range(cell-i):      
            time.sleep(0.05) 
            print(" ", end ="") 
        for k in range(2 * i-1): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
  
    for i in range(cell-1, 0, -1): 
        for j in range(cell-i): 
            time.sleep(0.05) 
            print(" ", end ="") 
              
        for k in range(2 * i-1): 
            time.sleep(0.05) 
            print("*", end ="") 
        print() 
diamond(n) 