# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:31:30 2017

@author: mimtiaz
"""
import numpy as np
import cv2
from skimage.feature import greycomatrix, greycoprops
import matplotlib.pyplot as plt



def glcmXbyXWinScan(sarraster, windowSize, step, angle):
#    sarfile = cv2.imread('8and1eyeDetect.jpg')
#    sarraster = sarfile[:,:,0]
    
    
    #Create rasters to receive texture and define filenames
    contrastraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    contrastraster[:] = 0.0
    
    dissimilarityraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    dissimilarityraster[:] = 0.0
    
    #homogeneityraster = np.copy(sarraster)
    homogeneityraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    homogeneityraster[:] = 0.0
    
    #energyraster = np.copy(sarraster)
    energyraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    energyraster[:] = 0.0
    
    #correlationraster = np.copy(sarraster)
    correlationraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    correlationraster[:] = 0.0
    
    #ASMraster = np.copy(sarraster)
    ASMraster = np.zeros((sarraster.shape[0], sarraster.shape[1]), dtype = float)
    ASMraster[:] = 0.0
    
    
    for i in xrange(sarraster.shape[0]):
#        print i,
        for j in xrange(sarraster.shape[1]):
            
            if i < windowSize or j <windowSize:
                continue
            # windows needs to fit completely in image
            if i > (contrastraster.shape[0] - windowSize) or j > (contrastraster.shape[1] - windowSize):
                continue
            
            # Define size of moving window
            glcm_window = sarraster[i-windowSize: i+windowSize, j-windowSize : j+windowSize]
            # Calculate GLCM and textures
            glcm = greycomatrix(glcm_window, step, angle,  symmetric = True, normed = True )
    
            # Calculate texture and write into raster where moving window is centered
            contrastraster[i,j]      = greycoprops(glcm, 'contrast')
            dissimilarityraster[i,j] = greycoprops(glcm, 'dissimilarity')
            homogeneityraster[i,j]   = greycoprops(glcm, 'homogeneity')
            energyraster[i,j]        = greycoprops(glcm, 'energy')
            correlationraster[i,j]   = greycoprops(glcm, 'correlation')
            ASMraster[i,j]           = greycoprops(glcm, 'ASM')
            glcm = None
            glcm_window = None
            
    #Normalization use when only needed   
    contrastraster = 255.0 * normalize(contrastraster)
    contrastraster = contrastraster.astype(int)
    
    dissimilarityraster = 255.0 * normalize(dissimilarityraster)
    dissimilarityraster = dissimilarityraster.astype(int)
    
    homogeneityraster = 255.0 * normalize(homogeneityraster)
    homogeneityraster = homogeneityraster.astype(int)
    
    energyraster = 255.0 * normalize(energyraster)
    energyraster = energyraster.astype(int)
    
    correlationraster = 255.0 * normalize(correlationraster)
    correlationraster = correlationraster.astype(int)
    
    ASMraster = 255.0 * normalize(ASMraster)
    ASMraster = ASMraster.astype(int)

    return contrastraster, dissimilarityraster, homogeneityraster, energyraster, correlationraster, ASMraster




def normalize(arrayX):
    for i in xrange(arrayX.shape[0]):
        for j in xrange(arrayX.shape[1]):
            arrayX[i,j] = ((arrayX[i,j] - arrayX.min()) / (arrayX.max() - arrayX.min()))
            
    return arrayX





#fake
image = cv2.imread('lena.png')
image = image[:,:,0]
#step = range(1,256)
#step = np.asarray(step)



#result = greycomatrix(image, step, [0,45,90,135], levels = 256, symmetric=True, normed=True) #, np.pi/4, np.pi/2, 3*np.pi/4
#, symmetric=True, normed=True
windowSz = 5
step = [1]      #step = range(1,10,2)

for i in range(0,180,45):
    print i
    angle = [i]
    contrastScan, dissimilarityScan, homogeneityScan, energyScan, correlationScan, ASMScan = glcmXbyXWinScan(image, windowSz, step, angle)
    
    contrastScan = contrastScan[windowSz : contrastScan.shape[0] - windowSz + 1, windowSz : contrastScan.shape[1] - windowSz + 1]
    dissimilarityScan = dissimilarityScan[windowSz : dissimilarityScan.shape[0] - windowSz + 1, windowSz : dissimilarityScan.shape[1] - windowSz + 1]
    homogeneityScan = homogeneityScan[windowSz : homogeneityScan.shape[0] - windowSz + 1, windowSz : homogeneityScan.shape[1] - windowSz + 1]
    energyScan = energyScan[windowSz : energyScan.shape[0] - windowSz + 1, windowSz : energyScan.shape[1] - windowSz + 1]
    correlationScan = correlationScan[windowSz : correlationScan.shape[0] - windowSz + 1, windowSz : correlationScan.shape[1] - windowSz + 1]
    ASMScan = ASMScan[windowSz : ASMScan.shape[0] - windowSz + 1, windowSz : ASMScan.shape[1] - windowSz + 1]
    
    #%%
    
    texturelist = {1: 'contrast', 2: 'dissimilarity', 3: ' homogeneity', 4: 'energy', 5: 'correlation', 6: 'ASM'}
    plt.figure(0+i)
    for key in texturelist:
        ax = plt.subplot(2,3,key)
        plt.axis('off')
        ax.set_title(texturelist[key])
        plt.imshow(eval(texturelist[key] + "Scan"), cmap = 'gray')
    
    plt.show(0+i)

