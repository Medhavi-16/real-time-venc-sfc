from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2

imageA = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/pic_new.jpg") 
imageB = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/final.jpg", 1)

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

print("SSIM: {}".format(score))
