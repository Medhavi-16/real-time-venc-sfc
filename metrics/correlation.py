import numpy as np
import pandas as pd
import cv2
import pathlib

def calc_corr(orig, enc):
	orig = pd.Series(orig.flatten())
	enc = pd.Series(enc.flatten())
	a = orig.corr(enc)
	b = enc.corr(orig)
	print(a, b)

def main():
    compressed = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/final.jpg", 1) 
    original = cv2.imread("/home/ankit/Desktop/Medhavi/BTP/real-time-venc-sfc/pic_new.jpg", 1)
    calc_corr(original, compressed)
       
if __name__ == "__main__": 
    main() 