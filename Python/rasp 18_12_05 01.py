# lea_01.py

import RPi.GPIO as GPIO
import time # 시간 정하기

# GPIO 관련 경고 메세지를 출력하지않음
GPIO.setwarnings(False)

# 핀번호 할당 방식을 BCM 핀 번호 방식으로 설정
GPIO.setmode(GPIO.BCM)
led_pin = 15

# 14번 핀을 출력핀 모드로 설정
GPIO.setup(14, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

# 14번으로 High 신호(3.3V)를 출력
GPIO.output(14, True)
GPIO.output(led_pin, False)
time.sleep(1)
GPIO.output(14, False)
GPIO.output(led_pin, True)
time.sleep(1)
GPIO.output(14, True)
GPIO.output(led_pin, False)
time.sleep(1)
GPIO.output(14, False)

# 사용된 GPIO 핀을 원래 상태로 되돌림
GPIO.cleanup()