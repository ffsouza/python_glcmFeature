# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:52:47 2017

@author: mimtiaz
"""

import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


with open('fileName.txt') as f:     #save directories in 'fileName.txt' of all files
    content = f.readlines()

#c = 0
for i in xrange(10, 11):       #len(content)
    img = cv2.imread((content[i])[:-1])
    img = img[:,:,0]
    
#    ret,thresh1 = cv2.threshold(img,127,1,cv2.THRESH_BINARY)
#    cv2.imwrite('test1.bmp', thresh1)
#    resizedImg = cv2.resize(thresh1, (4,4))
#    cv2.imwrite('test2.bmp', resizedImg)
    
    step = range(1,256)
    step = np.asarray(step)
#    step = [2]
    angle = [0,np.pi/2]
    coOccuranceMat = greycomatrix(img, step, angle, levels = 256, symmetric = True, normed = True )
#    coOccuranceMat = greycomatrix(resizedImg, step, angle, levels = 2, symmetric = True)
    
    #print coOccuranceMat[:,:,1,0]
    ll = coOccuranceMat[:,:,4,0]
    contrast = greycoprops(coOccuranceMat, 'contrast')
    dissimilarity = greycoprops(coOccuranceMat, 'dissimilarity')
    homogeneity = greycoprops(coOccuranceMat, 'homogeneity')
    energy = greycoprops(coOccuranceMat, 'energy')
    correlation = greycoprops(coOccuranceMat, 'correlation')
    ASM = greycoprops(coOccuranceMat, 'ASM')
    
    texturelist = {0: 'contrast', 1: 'dissimilarity', 2: ' homogeneity', 3: 'energy', 4: 'correlation', 5: 'ASM'}
    marker = {0: 'b-o', 1: 'r-^'}
    
    for j in range(0,6):
        c = 1
        for k in range(0, len(angle)):      #len(angle)
            plt.figure(j)
            plt.plot(step, eval(texturelist[j])[:,k], marker[k], alpha = 0.8)
    #        plt.plot(step, eval(texturelist[j])[:,0], 'b-*')
            plt.xlabel('distance from 1 ro 255')
            plt.ylabel(texturelist[j])
            plt.title(texturelist[j] + ' vs. distance')
            redPatch = mpatches.Patch(color = 'red', label = 'Angle at 90')
            bluePatch = mpatches.Patch(color = 'blue', label = 'Angle at 0')
            plt.legend(handles = [bluePatch, redPatch])
#            plt.xlim(0,256)
#            plt.ylim(-1.5,1.5)
            plt.show(j)
            
            
            c = c +1