# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:26:18 2017

@author: Mohammad Imtiaz
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops
#from skimage import data



def glcmXbyXWinScan(sarraster, windowSize):
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
        print i,
        for j in xrange(sarraster.shape[1]):
            
            if i < windowSize or j <windowSize:
                continue
            # windows needs to fit completely in image
            if i > (contrastraster.shape[0] - windowSize) or j > (contrastraster.shape[1] - windowSize):
                continue
            
            # Define size of moving window
            glcm_window = sarraster[i-windowSize: i+windowSize, j-windowSize : j+windowSize]
            # Calculate GLCM and textures
            glcm = greycomatrix(glcm_window, [1], [0],  symmetric = True, normed = True )
    
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


img = cv2.imread('Strauss_GL (83)_FlatIris.pgm')
imgM = cv2.imread('Strauss_GL (83)_FlatMask.pgm')

img = img[:,:,0]
imgM = imgM[:,:,0]

glcm = greycomatrix(img, [1], [0],  symmetric = True, normed = True )
contrast = greycoprops(glcm, 'contrast')
dissimilarityraster = greycoprops(glcm, 'dissimilarity')
homogeneityraster = greycoprops(glcm, 'homogeneity')
energyraster = greycoprops(glcm, 'energy')
correlationraster = greycoprops(glcm, 'correlation')
ASMraster = greycoprops(glcm, 'ASM')            

windowSz = 15       # change the window size based on need
contrastScan, dissimilarityScan, homogeneityScan, energyScan, correlationScan, ASMScan = glcmXbyXWinScan(img, windowSz)



texturelist = {1: 'contrast', 2: 'dissimilarity', 3: ' homogeneity', 4: 'energy', 5: 'correlation', 6: 'ASM'}
for key in texturelist:
    ax = plt.subplot(2,3,key)
    plt.axis('off')
    ax.set_title(texturelist[key])
    plt.imshow(eval(texturelist[key] + "Scan"), cmap = 'gray')

plt.show()







