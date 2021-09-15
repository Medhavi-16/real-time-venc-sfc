from matplotlib import pyplot as plt 
import cv2 

img = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/final.jpg", 1) 

plt.hist(img.ravel(),256,[0,256]) 

plt.show() 