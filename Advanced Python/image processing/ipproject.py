

import cv2
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

OutputFileName =open(r'C:/Users/anany/Desktop/VIT/semester 5/python lab/Advanced Python/image processing/imageprocessingsheet.xlsx', 'w')
OutputFileName.write("File Name"+","+","+",".join(proplist)+ '\n')
path = r"C:/Users/anany/Desktop/VIT/semester 5/python lab/Advanced Python/image processing/image.png"
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
cv2.imshow("unknown.png", unknown)
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