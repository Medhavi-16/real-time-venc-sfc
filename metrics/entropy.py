import skimage.measure  
import cv2 
import numpy as np   


def calc_entropy(orig, enc):
	entropy_org = skimage.measure.shannon_entropy(orig)
	entropy_enc = skimage.measure.shannon_entropy(enc)
	print('Entropy of Original Frame: ', entropy_org)
	print('Entropy of Encrypted Frame: ', entropy_enc)

def main():  
    compressed = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/pic_new.jpg", 1) 
    original = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/final.jpg", 1) 
    calc_entropy(original, compressed) 

if __name__ == "__main__": 
    main() 