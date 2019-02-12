#!/usr/bin/env python3

import socket
import io
import binascii
import cv2
import imutils
from skimage.measure import compare_ssim
import time

### Custom recv function to recieve until a newline character
### Not efficient but gets the job done
### Needed because not all data could be collected in a single recv()
### and parsing was a big challenge when it would sometimes collect 2 lines 
def recvline(sock):
        answer =b''
        while(True):
                d = sock.recv(1)
                if(d == b'\n'):
                        break
                answer += d
        return answer

CHAR_WIDTH=30

### Each glyph is 30px wide.
### Each letter is also saved individually in the letters/ directory
### opens the image in openCV, splits it up into a distinct segment for each glyph
### Then cycles through each letter and does SSIM (Structure Similarity Index) comparison
### If the "score" (likeness) is above 0.85 (on a scale of -1-1) it counts as a hit
### In this instance, a hit will always be a solid 1.0 because they are exact matches
### if it is a hit, it just adds the letter to the answer
### Returns the answer
def compareImage():
        answer = ''
        imA = cv2.imread('img_captcha.png')
        height, width = imA.shape[:2]
        WIDTH = int(width / 30)
        for i in range(1, WIDTH+1):
                #Parse and save!
                start_r = 0
                start_c = (i-1)*CHAR_WIDTH
                end_r, end_c = int(height), int(i*CHAR_WIDTH)
                new_img = imA[start_r:end_r, start_c:end_c]
                for j in range(ord('A'), ord('Z')+1):
                        imB = cv2.imread("letters/{}.png".format(chr(j)))
                        grayA = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imB, cv2.COLOR_BGR2GRAY)
                        (score,diff) = compare_ssim(grayA, grayB, full=True)
                        diff = (diff*255).astype('uint8')
                        if score > 0.85:
                                answer += chr(j)
                                break
        return answer



### The core of the code, create a socket, recv an image, save it correctly,
### Call the compareImage() function and return the result to the server!
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('misc.ctf.nullcon.net', 6001))
        print(s.recv(4096))
        print(s.recv(4096))
        s.sendall('\r\n'.encode('utf-8'))
        data = s.recv(4096)
        data = data +s.recv(4096)
        getbytes = binascii.unhexlify(data)
        f = open('img_captcha.png', 'wb')
        f.write(getbytes)
        f.close()
        print(s.recv(4096))
        s.sendall(compareImage().encode('utf-8') + b'\n')
        for i in range(199):
                print(s.recv(10)) #Correct!\r\n
                print(s.recv(4096))
                s.sendall(b'\r\n')
                data = recvline(s)
                data = data.decode('utf-8').strip()
                print("Data length: {}".format(len(data)))
                getbytes = binascii.a2b_hex(data)
                f = open('img_captcha.png', 'wb')
                f.write(getbytes)
                f.close()
                print(s.recv(4096))
                s.sendall(compareImage().encode('utf-8') + b'\n')
        print(s.recv(10)) #Correct!\r\n
        print(s.recv(4096))
        s.sendall(b'\r\n')
        print(s.recv(4096)) # FLAG