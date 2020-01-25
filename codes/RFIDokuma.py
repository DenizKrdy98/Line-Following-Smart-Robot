
#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


print "Hold a tag near the reader"
def okuma():
	id, x = reader.read()
	return x
try:
    print "sa"

finally:
    GPIO.cleanup()
