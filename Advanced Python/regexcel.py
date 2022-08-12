import openpyxl
import math
path="sample.xlsx"
wbobj=openpyxl.load_workbook(path)
sheet =wbobj.active
data=[]
for row in data:
    sheet.append(row)
row=sheet[2]
rowlist=[row[x].value for x in range(2,len(row))]
print("original list is: \n")
print(rowlist)
print("\n")
def quicksort(row_list):
    if row_list==[]:
        return []
    pivot=row_list[0]
    less=[]
    greater=[]
    for item in row_list[1:]:
        if item<pivot:
            less.append(item)
        else:
            greater.append(item)
    sortedlist=quicksort(less)+[pivot]+quicksort(greater)
    return sortedlist
finallist=quicksort(rowlist)
print("sorted list is: \n")
print(finallist)
print("\n")

def variance(finallist):
    mean=sum(finallist)/len(finallist)
    vari=sum((i-mean)**2 for i in finallist)/len(finallist)
    return str(vari)
vari=variance(rowlist)
print("variance is : \n")
print(vari)



def higerorder_variance(finallist):
    mean = sum(finallist) / len(finallist)
    var = 0
    for i in range(len(finallist)):
        var = var + (finallist[i] - mean) ** 2
    var = var / len(finallist)
    return var

print(higerorder_variance(rowlist))

def recursion_var(finallist, i):
    t = len(finallist)
    mean = sum(finallist) / t
    if i == t - 1:
        return ((finallist[0] ** 2) - (2 * mean * finallist[0]) + (mean ** 2))
    else:
        return ((finallist[t - i - 1] ** 2) - (2 * mean * finallist[t - i - 1])) + (mean ** 2) + (recursion_var(finallist, i + 1))
print("Variance of column using recursion is: ", str(recursion_var(rowlist, 0) / (len(rowlist)-1)))




column = sheet['B']
columnlist=[column[x].value for x in range(1,len(column))]
print("column 1 is: \n")
print(columnlist)
print("\n")
column = sheet['C']
columnlist1=[column[x].value for x in range(1,len(column))]
print("column 2 is: \n")
print(columnlist1)
print("\n")


def correlation(columnlist, columnlist1):
    mean1=sum(columnlist)/len(columnlist)
    mean2=sum(columnlist1)/len(columnlist1)
    listi1=[(i-mean1) for i in columnlist]
    listi2=[(j-mean2) for j in columnlist1]
    multiply=[]
    for number1, number2 in zip(listi1, listi2):
        multiply.append(number1*number2)
    corr1=sum(multiply)
    corr2=math.sqrt(sum((i-mean1)**2 for i in columnlist)*(sum((j-mean2)**2 for j in columnlist1)))
    correlationvalue=corr1/corr2
    return str(correlationvalue)
correlationvalue=correlation(columnlist, columnlist1)
print("correlation is : \n")
print(correlationvalue)
print("\n")


def regression(columnlist, columnlist1):
    multiply=[]
    n=len(columnlist)
    for number1, number2 in zip(columnlist, columnlist1):
        multiply.append(number1*number2)
    bdown=(n*(sum((i**2) for i in columnlist)))-(sum(columnlist)**2)
    a=((sum(columnlist1)*sum((i**2) for i in columnlist))-(sum(columnlist)*sum(multiply)))/bdown
    b=((n*(sum(multiply)))-((sum(columnlist))*(sum(columnlist1))))/bdown
    equation = "y=" + str(a) + "+" + str(b) +"x"
    return str(equation)
equation=regression(columnlist, columnlist1)
print("regression is : \n")
print(equation)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    