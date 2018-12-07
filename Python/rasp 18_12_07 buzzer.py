import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gpio_pin = 13
# 계이름 주파수에 맞춰 입력 a b c d e f g a2 도레미파솔라시도
a, b, c, d, e, f, g, a2 = 261, 294, 329, 349, 392, 440, 493, 523
scale = [261, 294, 329, 349, 392, 440, 493, 523]
GPIO.setup(gpio_pin, GPIO.OUT)

# 학교 종이 땡땡땡
schoolbell = [c, b, a, b, c, c, c, b, b, b, c, c, c, c, b, a, b, c, c, c, b, b, c, b, a]

# 곰세마리
## 음계
bear = [a, a, a, a, a, c, e, e ,c, a,
        e, e, c, e, e, c, a, a, a,
        e, e, c, a, e, e, e,
        e, e, c, a, e, e, e,
        e, e, c, a, e, e, e, f, e,
        a2, e, a2, e, c, b, a]

## 박자
bear_del = [0.4, 0.2, 0.2, 0.4, 0.4, 0.4, 0.2, 0.2, 0.4, 0.4, 
         0.2, 0.2, 0.4, 0.2, 0.2, 0.4, 0.4, 0.4, 0.8,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8,
         0.4, 0.4, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.8,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8]

## 가사
bear_lyric = '곰세마리가한집에있어아빠곰엄마곰애기곰\
아빠곰은뚱뚱해엄마곰은날씬해애기곰은너무귀여워으쓱으쓱잘한다'

p = GPIO.PWM(gpio_pin, 523) # 주파수 : 523Hz

p.start(70) # duty cycle : high의 비율

try:
    # for i in schoolbell:
    #    p.ChangeFrequency(i)
    #    time.sleep(0.1)
    for i in range(len(bear)):
        print(bear_lyric[i], end='')
        p.ChangeFrequency(bear[i])
        time.sleep(bear_del[i])
        
finally:
    p.stop()
    GPIO.cleanup()

