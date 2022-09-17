
#QUESTION 1
#CONTAINS IMAGEPROCESSING USING NUMPY AND NUMPY ARRAY MANIPULATIONS USING DATAFRAME

import cv2
import pandas as pd
#import io,os
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
#import glob
 
pixels_to_um =0.5
 
proplist = ['Area',
            'equivalent_diameter',
            'orientation',
            'MajorAxisLength',
            'MinorAxisLength',
            'Perimeter',
            'MinIntensity',
            'MeanIntensity',
            'MaxIntensity']

OutputFileName =open(r'sheetf1.csv', 'w')
OutputFileName.write("File Name"+","+",".join(proplist)+ '\n')
path = r"image.tif"
#for file in glob.glob(path):
 #print(file)
#Read  the File

src = cv2.imread(path) 

#cv2.waitKey(0)
window_name = 'Image'
#Preprocessing
image = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow("window_name", image)
pixels_to_um = 0.5
    
#Distance Transform and Thresholding
res ,thres =cv2.threshold(image ,0 ,255 ,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN,kernel,iterations =2)
 
#Distance Transform and Thresholding
   
sure_bg = cv2.dilate(opening, kernel, iterations=1)#change the parameter
dist_transform = cv2.distanceTransform(opening ,cv2.DIST_L2,3)#change the parameter
ret2, sure_fg = cv2.threshold(dist_transform,0.01*dist_transform.max(),255,0)#change the parameter
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow("unknown.tif", unknown)
cv2.waitKey(0)
#Markers
    
ret3, markers = cv2.connectedComponents(sure_fg)
markers =markers+10
markers[unknown ==255] =0
markers =cv2.watershed(src,markers)
src[markers == -1] = [0,255,255]
img2 =color.label2rgb(markers, bg_label =0)
 
 
regions =measure.regionprops(markers,intensity_image =image)
 
  
grain_number =1
for region_props in regions:
        #OutputFileName.write(file+",")
    OutputFileName.write(str(grain_number) + ',')
    for i,prop in enumerate(proplist):
        if(prop == 'Area'):
            to_print = region_props[prop]*pixels_to_um**2
        elif(prop == 'orientation'):
            to_print = region_props[prop]*57.2958
        elif(prop.find('Intensity')<0):
            to_print = region_props[prop]*pixels_to_um
        else:
            to_print = region_props[prop]           
        OutputFileName.write(','+str(to_print))
    OutputFileName.write('\n')
    grain_number +=1
OutputFileName.close()


#NUMPY USAGE

# convert datafram to numpy array
print('csv to dataframe')
dataframe1 = pd.read_csv('sheetf1.csv')
 
print(dataframe1)
print('\n')
print('\n')
print('\n')

print('df to array')
result = dataframe1.to_numpy()
print(result)

print('\n')
print('\n')
print('\n')

#convert one column of dataframe to numpy array
print('columns of df to array')
df2=dataframe1['Area'].to_numpy()
df3=dataframe1['equivalent_diameter'].to_numpy()

print(df2)

print('\n')
print('\n')
print('\n')
print(df3)

print('\n')
print('\n')
print('\n')

#convert array to numpy array
arr1 = np.array(result)
arr2 = np.array(df2)
arr3 = np.array(df3)
print('convert full dataframe to numpy array')
print(arr1)
print('\n')
print('\n')
print('\n')
print('one df column to numpy array')
print(arr2)
print('\n')
print('\n')
print('\n')
print(arr3)
print('\n')
print('\n')
print('\n')


#numpy array indexing
print('numpy array indexing')
print(arr1[0])

print('\n')
print('\n')
print('\n')

print(arr1[2] + arr1[3])

print('\n')
print('\n')
print('\n')

#numpy array slicing
print('numpy array slicing')
print(arr1[1:5])
print('\n')
print('\n')
print('\n')

print(arr1[-3:-1])
print('\n')
print('\n')
print('\n')

print(arr1[1:5:2])
print('\n')
print('\n')
print('\n')

print(arr1[1, 1:4])
print('\n')
print('\n')
print('\n')

#Numpy array datatypes
print('Numpy array datatype')
print(arr1.dtype)
print('\n')
print('\n')
print('\n')

#copy and view
x = arr1.copy()
arr1[0, 2] = 526.91800
print('copy and view')
print(x)
print('\n')
print('\n')
print('\n')

print(arr1)

print('\n')
print('\n')
print('\n')

#numpy array shape
print('numpy array shape')
print(arr1.shape)


print('\n')
print('\n')
print('\n')



#spliting array
print('spliting array')
newarr = np.array_split(arr1, 3)
print(newarr)
print('\n')
print('\n')
print('\n')

#search array
print('search an array')
x = np.where(arr1%2 == 0)
print(x)
print('\n')
print('\n')
print('\n')

#sort
print('sort an array')
print(np.sort(arr2))
print('\n')
print('\n')
print('\n')

# Create an empty list
print('using filtering array')
filter_arr = []
# go through each element in arr
for element in arr2:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr2[filter_arr]
print(filter_arr)
print('\n')
print('\n')
print('\n')

print(newarr)
print('\n')
print('\n')
print('\n')


#join numpy arrays
print('join numpy arrays')
arrjoin = np.concatenate((arr2, arr3))
print(arrjoin)

print('\n')
print('\n')
print('\n')

#reshape numpy array
print('reshape numpy array')
newarr = arrjoin.reshape(2, 5)
print(newarr)
