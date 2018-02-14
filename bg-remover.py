import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_bgd(img, points):
    b,g,r = cv2.split(img)       # get b,g,r
    img = cv2.merge([r,g,b])

    marked = cv2.watershed(img, points)

    marked[marked == 1] = 0
    marked[marked > 1] = 255

    kernel = np.ones((3,3),np.uint8)
    dilation = marked

    dilation = cv2.dilate(dilation.astype(np.float32), kernel, iterations = 1)

    masked_data = cv2.bitwise_and(img, img, mask=dilation.astype(np.uint8))

    b,g,r = cv2.split(masked_data)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])

    cv2.imwrite("result_img.png", rgb_img)
    # plt.imshow(rgb_img)
    # plt.show()



if __name__ == "__main__":
    img = cv2.imread("295bn7l.png", 3)

    marker = np.zeros_like(img[:,:,0]).astype(np.int32)

    # Rear red-light
    marker[190][454] = 64

    # rooftop
    marker[135][294] = 64

    # rear bumper
    marker[225][456] = 128
    marker[224][461] = 128
    marker[216][461] = 128

    # EVERYTHING
    marker[235][370] = 255

    # rear wing
    marker[167][458] = 64

    # front wheel
    marker[225][189] = 192
    marker[240][147] = 192

    # rear wheel
    marker[258][409] = 192
    marker[257][391] = 192
    marker[254][421] = 192

    # front bumper
    marker[205][103] = 128


    marker[240][137] = 1
    marker[245][444] = 1
    marker[260][427] = 1
    marker[257][378] = 1
    marker[204][95] = 1
    marker[217][466] = 1

    remove_bgd(img, marker)
