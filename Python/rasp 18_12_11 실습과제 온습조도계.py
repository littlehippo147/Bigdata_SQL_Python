# i2c와 LCD 이용 온습도, 조도 출력
import RPi.GPIO as GPIO
import smbus2 as smbus
import time

############################ LCD Base
# Define GPIO to LCD mapping
LCD_RS = 23
LCD_E  = 26 
LCD_D4 = 17
LCD_D5 = 18
LCD_D6 = 27
LCD_D7 = 22


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7
###########################
########################### i2c temp_humi Base
DEVICE = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21

bus = smbus.SMBus(1) # 채널 1번으로 smbus객체생

addr = 0x40

cmd_temp = 0xf3  # temp cmd 1111 0011
cmd_humi = 0xf5  # humi cmd 1111 0101
soft_reset = 0xfe  # 1111 1110
data = [0,0]

bus.write_byte(addr,soft_reset) # reset 초기화
time.sleep(0.5)
##########################
########################## LCD function definition
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

########################## main function definition
def main():
    # Initialise display
    lcd_init()

    while True:
        # 조도 측정
        data = bus.read_i2c_block_data(DEVICE,ONE_TIME_HIGH_RES_MODE_1,2)
        result = round(((data[0]*256) + data[1])/1.2,2)
        
        # 온도 측정
        bus.write_byte(addr,cmd_temp) 
        time.sleep(0.260)
        
        for i in range(2):
            data[i] = bus.read_byte(addr)
            
        val = data[1] + (data[0]<<8)
        temp = round((-46.85 + (175.72*val)/65536),2)
        

        # 습도 측정
        bus.write_byte(addr,cmd_humi) 
        time.sleep(0.260)

        for i in range(2):
            data[i] = bus.read_byte(addr)
            
        val = data[1] + (data[0]<<8)
        humi = round((-6.0 + (125.0*val)/65536),2)

        lcd_string('T : ' + str(temp) + 'H : ' + str(humi), LCD_LINE_1)
        lcd_string('L : ' + str(result), LCD_LINE_2)
        print('temp :', temp, 'humi :', humi, 'lx :', result)
        time.sleep(0.5)

##########################
########################## main 실행

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()

