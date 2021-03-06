# raspberryPi Flask ultrasonic
from flask import Flask, render_template
import datetime
import time
import RPi.GPIO as GPIO
import smbus2 as smbus
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings( False )

########################### i2c temp_humi Base
DEVICE = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21

bus = smbus.SMBus(1) # smbus

addr = 0x40

cmd_temp = 0xf3  # temp cmd 1111 0011
cmd_humi = 0xf5  # humi cmd 1111 0101
soft_reset = 0xfe  # 1111 1110
data = [0,0]

bus.write_byte(addr,soft_reset) # reset initialize
time.sleep(0.5)

##########################
########################## led
led_pins = [ 14, 15 ]
led_states = [ 0, 0 ]
GPIO.setup( led_pins[0], GPIO.OUT )
GPIO.setup( led_pins[1], GPIO.OUT )

def update_leds():
    for i, value in enumerate( led_states ):
        GPIO.output( led_pins[i], value )

##########################

# main hello
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   
   # temp measure
   bus.write_byte(addr,cmd_temp) 
   time.sleep(0.260)
    
   for i in range(2):
       data[i] = bus.read_byte(addr)
        
   val = data[1] + (data[0]<<8)
   temp = round((-46.85 + (175.72*val)/65536),2) # temp computing
   
   # templatedata input
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'temp': temp
   }
   return render_template('main.html', **templateData)
# ultrasonic
@app.route("/ultrasonic")
def ultrasonic():
   try:
      trig = 0
      echo = 1

      GPIO.setup(trig, GPIO.OUT)
      GPIO.setup(echo, GPIO.IN)
      
      # trigger output
      GPIO.output(trig, False) # Low
      time.sleep(0.5)
      GPIO.output(trig, True)  # High
      time.sleep(1*0.00001)      # 10 us / duration
      GPIO.output(trig, False)

      # echo input
      while GPIO.input(echo) == False:
          pulse_start = time.time()
          
      while GPIO.input(echo) == True:
          pulse_end = time.time()

      pulse_duration = pulse_end - pulse_start
      distance = round((pulse_duration * 17000), 2)
        
      response = 'Disdance is ' + str(distance) + 'cm!'
   
   except: # except message
      response = "There was an error measuring distance."

   templateData = {
      'title' : 'Ultrasonic Distance',
      'response' : response
      }

   return render_template('ultrasonic.html', **templateData)
# led
@app.route('/<led>')
def index( led = "n" ):
   if led != "n":
        led_num = int( led )
        led_states[led_num] = not led_states[led_num]
        update_leds()

   now = datetime.datetime.now()
   timeString = now.strftime( "%Y-%m-%d %H:%M:%S" )

   pin_num = 14
   ledString = "Pin status  "
   for state in led_states:
       if state == 0:
           ledString += "[ "
           ledString += str( pin_num )
           ledString += " is Off "
       else:
           ledString += "[ "
           ledString += str( pin_num )
           ledString += " is On "
       ledString += " ] "
       pin_num = pin_num + 1
   ledString += "   "

   templateData = {
            'title' : 'LED Control',
            'time' : timeString,
            'led_status' : ledString,
            }
   return render_template( 'led.html', **templateData )

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


