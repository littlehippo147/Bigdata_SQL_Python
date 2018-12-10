# Passive infrared sensor(적외선 센서)
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pir = 24
gpio_pin = 13
GPIO.setup(pir, GPIO.IN)
GPIO.setup(gpio_pin, GPIO.OUT)

p = GPIO.PWM(gpio_pin, 392) # 솔


def loop():
    cnt = 0
    while True:
        if (GPIO.input(pir) == True):
            print('detected %d' %cnt)
            cnt += 1
            
            p.start(70)
            time.sleep(0.05)
            p.stop()
        time.sleep(0.05)
        
        
try:
    loop()
    
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()