import numpy as np
import cv2

def color_recognize(img_path):
    img = cv2.imread(img_path) # bgr
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)