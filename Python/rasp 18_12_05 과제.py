# rasp 18_12_05 과제.py

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def led_init(led1, led2) :
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    
def led_on(led_pin) :
    GPIO.output(led_pin, True)
    
def led_off(led_pin) :
    GPIO.output(led_pin, False)
    
def led_blink(led_pin, delay) :
    led_on(led_pin)
    time.sleep(delay)
    led_off(led_pin)

def led_shift(led1, led2, delay) :
    led_on(led1)
    time.sleep(delay)
    led_off(led1)
    led_on(led2)
    time.sleep(delay)
    led_off(led2)
    
if __name__ == "__main__" :
    try :
        led1, led2 = 14, 15
        led_init(led1, led2)
        
        led_off(led1); led_off(led2)
        print("led initializing")
        time.sleep(2)
        led_on(led1)
        print("led1 on")
        time.sleep(2)
        led_off(led1)
        print("led1 off")
        time.sleep(2)
        led_on(led2)
        print("led2 on")
        time.sleep(2)
        led_off(led2)
        print("led2 off")
        time.sleep(2)
        led_blink(led1,0.5)
        print("led1 blink")
        time.sleep(2)
        led_blink(led2,0.5)
        print("led2 blink")
        time.sleep(2)
        led_shift(led1, led2, 0.5)
        led_shift(led1, led2, 0.5)
        print("led1,2 twinkle twinkle")
        time.sleep(2)
        
        s = time.time()
        e = time.time()
        print("Burning!!!")
        while e - s <= 5:
            led_shift(led1, led2, 0.05)
            e = time.time()
        
    finally :
        print("실행 종료\n")
        GPIO.cleanup()