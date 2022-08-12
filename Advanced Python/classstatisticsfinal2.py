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

##############################################

#STATISTICS CLASS (SUPER CLASS)
class Statistics():
    def __init__(self, mean1, mean2):
        self.mean1=mean1
        self.mean2=mean2

#VARIANCE CLASS  
class Variance(Statistics): 
    def __init__(self, finallist, rowlist, mean1, mean2):
        super().__init__(mean1, mean2)
        self.finallist=finallist
        self.rowlist=rowlist


#POPULATION VARIANCE
    def variance(self, arg):
        mean=sum(self.finallist)/len(self.finallist)
        vari=sum((i-mean)**2 for i in self.finallist)/len(self.finallist)
        return str(vari)

#SAMPLE VARIANCE
    def variancesample(self, arg):
        mean=sum(self.finallist)/len(self.finallist)
        varisample=sum((i-mean)**2 for i in self.finallist)/(len(self.finallist)-1)
        return str(varisample)
    
#POPULATION VARIANCE HIGHER ORDER RECURSION
    def higerorder_variance(self, arg):
        mean = sum(self.finallist) / len(self.finallist)
        var = 0
        for i in range(len(self.finallist)):
            var = var + (self.finallist[i] - mean) ** 2
        var = var / len(self.finallist)
        return var
    
#SAMPLE VARIANCE HIGHER ORDER RECURSION
    def higerorder_variancesample(self, arg):
        mean = sum(self.finallist) / len(self.finallist)
        varsample = 0
        for i in range(len(self.finallist)):
            varsample = varsample + (self.finallist[i] - mean) ** 2
        varsample = varsample / (len(self.finallist)-1)
        return varsample
  
#CORRELATION DERIVED CLASS
class Correlation(Statistics): 
    def __init__(self, columnlist, columnlist1, mean1, mean2):
        super().__init__(mean1, mean2)
        self.columnlist=columnlist
        self.columnlist1=columnlist1

#PEARSON CORRELATION
    def correlation(self, arg, args):
        listi1=[i for i in self.columnlist]
        listi2=[j for j in self.columnlist1]
        multiply=[]
        for number1, number2 in zip(listi1, listi2):
            multiply.append(number1*number2)
        corr1=(len(self.columnlist)*sum(multiply)) - ((sum(self.columnlist))*(sum(self.columnlist1)))
        part1=math.sqrt((len(self.columnlist)*(sum(i**2 for i in self.columnlist)))-((sum(self.columnlist))**2))
        part2=math.sqrt((len(self.columnlist1)*(sum(i**2 for i in self.columnlist1)))-((sum(self.columnlist1))**2))
        corr2= part1*part2
        correlationvalue=corr1/corr2
        return str(correlationvalue)
    
#SAMPLE CORRELATION  
    def samplecorrelation(self, arg, args):
        
        listi1=[(i-self.mean1) for i in self.columnlist]
        listi2=[(j-self.mean2) for j in self.columnlist1]
        multiply=[]
        for number1, number2 in zip(listi1, listi2):
            multiply.append(number1*number2)
        upper=(sum(multiply))/(len(columnlist)-1)
        s1= math.sqrt((sum((i-self.mean1)**2 for i in self.columnlist))/(len(self.columnlist)-1))
        s2= math.sqrt((sum((j-self.mean2)**2 for j in self.columnlist1))/(len(self.columnlist1)-1))
        down=s1*s2
        samcorrelationvalue=upper/down
        return str(samcorrelationvalue)
    
#LINEAR CORRELATION
    def lincorrelation(self, arg, args):
        listi1=[i for i in self.columnlist]
        listi2=[j for j in self.columnlist1]
        multiply=[]
        for number1, number2 in zip(listi1, listi2):
            multiply.append(number1*number2)
        corr1=(len(self.columnlist)*sum(multiply)) - ((sum(self.columnlist))*(sum(self.columnlist1)))
        part1=math.sqrt((len(self.columnlist)*(sum(i**2 for i in self.columnlist)))-((sum(self.columnlist))**2))
        part2=math.sqrt((len(self.columnlist1)*(sum(i**2 for i in self.columnlist1)))-((sum(self.columnlist1))**2))
        corr2= part1*part2
        lincorrelationvalue=corr1/corr2
        return str(lincorrelationvalue)
    
    
#POPULATION CORRELATION
    def popcorrelation(self, arg, args):
        listi1=[(i-self.mean1) for i in self.columnlist]
        listi2=[(j-self.mean2) for j in self.columnlist1]
        multiply=[]
        for number1, number2 in zip(listi1, listi2):
            multiply.append(number1*number2)
        upper=(sum(multiply))/(len(columnlist))
        s1= math.sqrt((sum((i-self.mean1)**2 for i in self.columnlist))/(len(self.columnlist)))
        s2= math.sqrt((sum((j-self.mean2)**2 for j in self.columnlist1))/(len(self.columnlist1)))
        down=s1*s2
        popcorrelationvalue=upper/down
        return str(popcorrelationvalue)

#REGRESSION DERIVED CLASS
class Regression(Statistics): 
    def __init__(self, columnlist, columnlist1, mean1, mean2):
        super().__init__(mean1, mean2)
        self.columnlist=columnlist
        self.columnlist1=columnlist1
        
#REGRESSION  
    def regression(self, arg, args):
        multiply=[]
        n=len(self.columnlist)
        for number1, number2 in zip(self.columnlist, self.columnlist1):
            multiply.append(number1*number2)
        bdown=(n*(sum((i**2) for i in self.columnlist)))-(sum(self.columnlist)**2)
        a=((sum(self.columnlist1)*sum((i**2) for i in self.columnlist))-(sum(self.columnlist)*sum(multiply)))/bdown
        b=((n*(sum(multiply)))-((sum(self.columnlist))*(sum(self.columnlist1))))/bdown
        equation = "y=" + str(a) + "+" + str(b) +"x"
        return str(equation)

#constructing an object instance
genobj1 = Variance(finallist, rowlist, mean1, mean2)
genobj2=Correlation(columnlist, columnlist1, mean1, mean2)
genobj3=Regression(columnlist, columnlist1, mean1, mean2)

#accessing attribute values
print("Variance sample: ")
print(genobj1.variance(rowlist))
print("Variance sample higher order: ")
print(genobj1.higerorder_variance(rowlist))
print("Variance population: ")
print(genobj1.variancesample(finallist))
print("Variance population higher order: ")
print(genobj1.higerorder_variancesample(finallist))

print("Pearson Correlation: ")
print(genobj2.correlation(columnlist, columnlist1))
print("Linear Correlation: ")
print(genobj2.lincorrelation(columnlist, columnlist1))
print("Sample Correlation: ")
print(genobj2.samplecorrelation(columnlist, columnlist1))
print("Population Correlation: ")
print(genobj2.popcorrelation(columnlist, columnlist1))

print("Regression: ")
print(genobj3.regression(columnlist, columnlist1))