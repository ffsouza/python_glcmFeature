# python_glcmFeature
This .py file describe how to use GLCM (Gray level co-occurrence matrix) to analyze texture information of an image 

GLCM represents texture information of an image with six different parameters:  1: 'contrast', 2: 'dissimilarity', 3: ' homogeneity', 4: 'energy', 5: 'correlation', 6: 'ASM'


For details follow this tutorial:
http://www.fp.ucalgary.ca/mhallbey/tutorial.htm


There is two way to use GLCM for mesuring texture:
1. to apply GLCM on the whole image. Here GLCM will give a single number for wach parameter which will reperesent the texture. 
2. crete a window, apply glcm on the widow pixels and by this scan the entire image. Here GLCM will give a 2D matrix approximatly close to the size of input image based on how this window has been used. Here more detail changes of texture can be found. 

Both of these ways has been implemented in the .py file.
