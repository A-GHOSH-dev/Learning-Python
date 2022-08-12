from classstatisticsfinal2 import Variance, Correlation, Regression
import openpyxl
path="newsheet.xlsx"
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

mean1=sum(columnlist)/len(columnlist)
mean2=sum(columnlist1)/len(columnlist1)

##############################################################

#VARIANCE
a = Variance(finallist, rowlist, mean1, mean2)
#POPULATION VARIANCE
print("Variance sample: ")
print(a.variance(rowlist))
#SAMPLE VARIANCE
print("Variance sample higher order: ")
print(a.variancesample(rowlist))
#POPULATION VARIANCE HIGHER ORDER RECURSION
print("Variance population: ")
print(a.higerorder_variance(rowlist))
#SAMPLE VARIANCE HIGHER ORDER RECURSION
print("Variance population higher order: ")
print(a.higerorder_variancesample(rowlist))

#CORRELATION
d = Correlation(columnlist, columnlist1, mean1, mean2)
#PEARSON CORRELATION
print("Pearson Correlation: ")
print(d.correlation(columnlist, columnlist1))
#SAMPLE CORRELATION 
print("Linear Correlation: ")
print(d.samplecorrelation(columnlist, columnlist1))
#LINEAR CORRELATION
print("Sample Correlation: ")
print(d.lincorrelation(columnlist, columnlist1))
#POPULATION CORRELATION
print("Population Correlation: ")
print(d.popcorrelation(columnlist, columnlist1))

#REGRESSION
g = Regression(columnlist, columnlist1, mean1, mean2)
print("Regression: ")
print(g.regression(columnlist, columnlist1))
