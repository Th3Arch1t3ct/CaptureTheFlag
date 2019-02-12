#!/usr/bin/env python3

import cv2
import numpy as np

CHAR_WIDTH=30

for j in range(22):
    # Read Each file
    image = cv2.imread('img_captcha{}.png'.format(j))
    height, width = image.shape[:2]
    WIDTH = int(width / 30)
    for i in range(1, WIDTH+1):
        #Parse and save!
        start_r = 0
        start_c = (i-1)*CHAR_WIDTH
        end_r, end_c = int(height), int(i*CHAR_WIDTH)
        new_img = image[start_r:end_r, start_c:end_c]
        cv2.imwrite('char_img_{}_{}.png'.format(j, i), new_img)
