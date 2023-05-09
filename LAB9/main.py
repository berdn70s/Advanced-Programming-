import cv2 as cv2
import numpy as np
import urllib.request 
url = "https://th.bing.com/th/id/R.2ba4d713d2aeb9940c172d319c26da7c?rik=yLLrzzeyHqBz8g&pid=ImgRaw&r=0"
with urllib.request.urlopen(url) as url_response:
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)

image = cv2.imdecode(img_array, -1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

green_chnl = image[:, :, 1]
red_chnl = image[:, :, 2]
blue_chnl = image[:, :, 0]

cv2.imshow('Red', red_chnl)
cv2.imshow('Green', green_chnl)
cv2.imshow('Blue', blue_chnl)


image[:, :, 2] += 40
image[:, :, 0] += 20
image[:, :, 1] = 30

image = np.clip(image, 0, 255)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow('lightning mcqueen', image)
cv2.waitKey(0)
