# raspberry pi 실습과제 spi 이용하기
import RPi.GPIO as GPIO
import spidev
import time

############################## LCD Base
trig = 0      # LCD pin setting
echo = 1
pir = 24
LCD_RS = 23
LCD_E  = 26 
LCD_D4 = 17
LCD_D5 = 18
LCD_D6 = 27
LCD_D7 = 22

LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

 # GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

##############################
############################## Spi
spi = spidev.SpiDev()
spi.open(0,1)
adc_read =[0,0,0]

def analog_read(ch): # ch : 00 01 10
	# 12 bit 
	r = spi.xfer2([0x6 | (ch & 0x7) >> 2, ((ch & 0x7) << 6),0 ])
	adcout= ((r[1] & 0xf) << 8) + r[2]

	# 10 bit
	#r= spi.xfer2([1, (8+channel)<<4, 0])
	#ret = ((r[1]&3) << 8) + r[2]
	return adcout

############################## LCD function definition
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

##############################
############################## get function definition
def get_cds_value():
    return analog_read(0)

def get_vr_value():
    return analog_read(1)

def get_sound_value():
    return analog_read(2)

##############################
############################## main function definition
def main():
    # Initialise display
    lcd_init()
    
    while 1:
        cds = get_cds_value() # 조도센서
        vr = get_vr_value() # 가변저항
        sound = get_sound_value() # 음성센서
        
        # lcd line1에 Cds, VR 출력
        lcd_string('Cds : ' + str(cds) + 'VR : ' + str(vr), LCD_LINE_1)
        print('Cds :', cds, 'VR :', vr)
        # lcd line2에 sound 출력
        lcd_string('Sound : ' + str(sound), LCD_LINE_2)
        print("sound :", sound)
        time.sleep(0.5)

############################## main function 실행
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()