import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure,color,io
#scikit-image
pixels_to_um = 0.5
proplist = ['area',
            'equivalent_diameter',
            'orientation',
            'majoraxislength',
            'minoraxislength',
            'perimeter',
            'minintensity',
            'meanintensity',
            'maxintensity']
OutputFileName = open(r'C:/Users/anany/Desktop/VIT/semester 5/python lab/Advanced Python/imageprocessingsheet.xlsx')
OutputFileName.write("File Name"+","+","+",".join(proplist)+ '\n')
img1 = cv2.imread("image.tiff")
img = cv2.cvtColor(img1,cv2.Color_BGR2GRAY)
pixels_to_um = 0.5
res, thres = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thres,cv2.MORPH_OPEN,kernel,iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations =1)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg = cv2.threshold(dist_transform,0.01*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow("unknown",unknown)
cv2.waitKey(0)
ret3, markers = cv2.connectedComponents(sure_fg)
markers = markers+10
markers[unknown ==255] =0
markers = cv2.watershed(img1,markers)
img1[markers == -1] = [0,255,255]
img2 = color.label2rgb(markers,bg_label = 0)
regions = measure.regionprops(markers,intensity_image = img)
grain_number = 1
for region_props in regions:
    OutputFileName.write(str(grain_number) + ',')
    for i,prop in enumerate(proplist):
        if(prop == 'area'):
            to_print =region_props[prop]
            pixels_to_um*2
        elif(prop == 'orientation'):
            to_print = region_props[prop]*57.2958
        elif(prop.find('Intensity')<0):
            to_print = region_props*pixels_to_um
        else:
            to_print = region_props[prop]
        OutputFileName.write(","+str(to_print))
    OutputFileName.write('\n')
    grain_number += 1
OutputFileName.close()