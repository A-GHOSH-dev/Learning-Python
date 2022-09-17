import matplotlib.pyplot as plt
import pandas as pd
var= pd.read_excel('C:\\Users\\name\\Documents\\officefiles.xlsx')
plt.plot(var['column name'])
print(var.head())
plt.show()