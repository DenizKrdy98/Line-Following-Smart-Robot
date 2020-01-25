
import cv2
from PIL import Image
import pytesseract
from time import sleep

def detect(): 
	IMAGE_FILE = '/home/pi/Desktop/ata/DUR.jpg'
 
	# loop forever
	while True:
 
    	# save image from webcam
    		img = cv2.VideoCapture(0).read()[1]
    		cv2.imwrite(IMAGE_FILE, img)
 
    	# load image
    		img = Image.open(IMAGE_FILE)
 
    	# detect words in image
    		words =pytesseract. image_to_string(img, config = 'psm --11').strip()
    		if words:   
			if "g" and  "h"  in words:
				print "saga girdim ben" , words
				words='right'
				break
			elif "e" and "t"   in words:
				print "sola girdim ben", words
				words='left'
				break
 			elif "o" or "w" or "a" or "d" in words:
				print "catla" , words
				words='forward'
				break
 
    			#words = None
 
    # annouce the arrival of Mr Puce! 
	return words 
	
