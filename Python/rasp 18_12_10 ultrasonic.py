# ultrasonic sensor
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig = 0
echo = 1

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# trigger 신호 출력
try:
    while True:
        GPIO.output(trig, False) # Low
        time.sleep(0.5)

        GPIO.output(trig, True)  # High
        time.sleep(1*0.00001)      # 10 us / duration

        GPIO.output(trig, False)

        # echo 신호 검출
        while GPIO.input(echo) == False:
            pulse_start = time.time()
            
        while GPIO.input(echo) == True:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = round((pulse_duration * 17000), 2)

        print("Distance :", distance, "cm")

finally:
    GPIO.cleanup()

