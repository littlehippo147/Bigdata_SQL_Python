# rasp 18_12_05 02.py

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# led의 핀번호를 지정
led_pin1 = 14
led_pin2 = 15

# led pin을 출력핀으로 설정 / 함수로 생성
def led_init(led1, led2):
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)

led_init(14, 15)

# led on/off 제어
for i in range(10):
    GPIO.output(led_pin1, True) # led off
    GPIO.output(led_pin2, True)
    time.sleep(0.2)
    GPIO.output(led_pin1, False)  # led on
    GPIO.output(led_pin2, False)
    time.sleep(0.2)

if __name__ == '__main__':
    try:
        s = time.time()
        e = time.time()
        while e-s <= 5:
            GPIO.output(led_pin1, False) # led off
            GPIO.output(led_pin2, False)
            time.sleep(0.05)
            GPIO.output(led_pin1, True)  # led on
            GPIO.output(led_pin2, True)
            time.sleep(0.05)
            e = time.time()
    finally:
        print("finally : GPIO Clean Up \n")
        GPIO.cleanup()




