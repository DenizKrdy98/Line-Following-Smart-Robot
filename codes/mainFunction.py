
# -*- coding: utf-8 -*-
import RPi.GPIO as IO
import time
import RFIDokuma
import QRscan
import imageRec


# MAIN MOVEMENT FUNCTIONS

def forward():
			IO.output(4,True) #1A+
                        IO.output(17,False) #1B-

                        IO.output(27,True) #2A+
                        IO.output(22,False) #2B-
def backwards():
			IO.output(4,False) #1A+
                        IO.output(17,True) #1B-

                        IO.output(27,False) #2A+
                        IO.output(22,True) #2B-

def right():
			IO.output(4,True)
                        IO.output(17,False)
                       	IO.output(27,True)
                        IO.output(22,True)
def left():
			IO.output(4,True)
                       	IO.output(17,True)
                       	IO.output(27,True)
                       	IO.output(22,False)
def still():
			IO.output(4,True) #1A+
                        IO.output(17,True) #1B-

                        IO.output(27,True) #2A+
                        IO.output(22,True) #2B-
def right90():
			right()
			time.sleep(1.9)
def left90():
			left()
			time.sleep(3.0)

IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setwarnings(False)

#IR PINS
IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out
IO.setup(21,IO.IN) #GPIO 21 -> Forward IR out

#MOTOR CONTROLLER PINS
IO.setup(4,IO.OUT) #GPIO 4 -> Motor Right terminal A
IO.setup(17,IO.OUT) #GPIO 14 -> Motor Right terminal B
IO.setup(27,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(22,IO.OUT) #GPIO 18 -> Motor Left terminal B

#ULTRASONIC SENSOR PINS
TRIG = 18
ECHO = 23
IO.setup(TRIG,IO.OUT)
IO.setup(ECHO,IO.IN)

#COUNTERS FOR TRACK ALGORITHM
a=0		#Right-hand Turn Control Counter
b=0		#Left-hand Turn Control Counter
z=0		#RUN Number Counter
y='null'	#Komut tipi degiskeni


# MAIN CODE

while True:
    #Distance Calculator
	IO.output(TRIG, False)
	time.sleep(0.1)
	IO.output(TRIG, True)
  	time.sleep(0.00001)
  	IO.output(TRIG, False)

	while IO.input(ECHO)==0:
    		pulse_start = time.time()

	while IO.input(ECHO)==1:
		pulse_end = time.time()

  	pulse_duration = pulse_end - pulse_start

 	distance = pulse_duration * 17150
  	distance = round(distance, 2)

	if distance < 15: # Obstacle Check
		still()

	else:
    		if(IO.input(2)==True and IO.input(3)==True): 	#both black, move forward
                	forward()

    		elif(IO.input(2)==True and IO.input(3)==False): #turn left
                	still()
                    	time.sleep(0.01)
                    	left()
	         	if(IO.input(21)==True):
	       	        	print 'Lefte devamliyorum'
				time.sleep(0.05)
    		elif(IO.input(2)==False and IO.input(3)==True): #turn right
			still()
                        time.sleep(0.01)
                        right()
            		if (IO.input(21)==True):
                		print 'Righta devamliyorum'
				time.sleep(0.05)
        	else:  #stay still
               		print "Cift beyaza girdim"  #Junction Point
			still()
            		while True:
				if ((a==0 and b ==0) or a==4 or b==4 or a==10):

			   	        print "Enter direction: "

					if z==0:
						y = RFIDokuma.okuma()		# - RFID
					elif z==1:
						y= QRscan.qr() 	                # - QR
					elif z==2:
						y= imageRec.detect()	 	# - IMAGE PROCESSING
					else:
						y=raw_input()                   # - keyboard input
						z=0

					y= "".join(y.split()) #Get rid of white spaces
					initial = y
					print "y equals to " ,  y
					print  "Inside of lap" , z

					z=z+1

					a=0
					b=0

                		if (y == 'right' or a==3 or b==1 or b==2 ):		 #TURN RIGHT
					still()
					time.sleep(0.5)
					print "Rightliyorum"
                    			right90()
					y='null'
					if (initial == 'right'):
						a=a+1
					else:
						b=b+1
                    			break

             	  		elif (y == 'left' or a==1 or a==2 or b==3 ):		 #TURN LEFT
					still()
					time.sleep(0.5)
					print "Leftliyorum"
					left90()
					y='null'
                    		 	if (initial == 'right'):
                                                a=a+1
                                        else:
                                                b=b+1
					break

				elif  (y == 'forward' or a==5) :
					print "Forwardliyorum"
					forward()
					time.sleep(0.1)
					a=a+5
 					break

                		else:
					print "y = " + y
                    			print "Invalid input, reenter: "


