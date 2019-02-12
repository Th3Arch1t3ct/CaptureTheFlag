#!/usr/bin/env python3

import socket
import io
import binascii
import cv2
import imutils
from skimage.measure import compare_ssim
from skimage.transform import rotate
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

degrees = [0, 45, -45]
scales = [1, 0.5, 1.5]

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
                        br,bc = grayB.shape
                        for degree in degrees:
                            matrix = cv2.getRotationMatrix2D((bc/2,br/2), degree, 1)
                            rot_temp = cv2.warpAffine(grayB, matrix, (bc,br))
                            for scale in scales:
                                scale_temp = cv2.resize(rot_temp, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
                                sc_h,sc_w = scale_temp.shape[:2]
                                sx = int(sc_w / 2) - 15
                                ex = sx + width
                                sy = int(sc_h / 2) - 15
                                ey = sy + height
                                scale_temp = scale_temp[sy:ey, sx:ex]
                                print(scale_temp.shape[:2])
                                print(grayA.shape[:2])
                                (score,diff) = compare_ssim(grayA, scale_temp, full=True)
                                diff = (diff*255).astype('uint8')
                                print("Score: {}".format(score))
                                if score > 0.60:
                                        print("Possible match: {}  on index {}".format(chr(j), i))
                                        answer += chr(j)
                                        break
        return answer


### The core of the code, create a socket, recv an image, save it correctly,
### Call the compareImage() function and return the result to the server!
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('miscc.ctf.nullcon.net', 6002))
            print(s.recv(4096))
            print(s.recv(4096))
            s.sendall('\r\n'.encode('utf-8'))
            data = recvline(s)
            data = data.decode('utf-8').strip()
            getbytes = binascii.unhexlify(data)
            f = open('img_captcha.png', 'wb')
            f.write(getbytes)
            f.close()
            print(s.recv(4096))
            s.sendall(compareImage().encode('utf-8') + b'\n')
            for i in range(199):
                    print(recvline(s)) #Correct!\r\n
                    print(recvline(s))
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

def getImage(rep):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('miscc.ctf.nullcon.net', 6002))
        print(s.recv(4096))
        print(s.recv(4096))
        s.sendall('\r\n'.encode('utf-8'))
        data = recvline(s)
        data = data.decode('utf-8').strip()
        getbytes = binascii.unhexlify(data)
        f = open('img_captcha{}.png'.format(rep), 'wb')
        f.write(getbytes)
        f.close()

main()