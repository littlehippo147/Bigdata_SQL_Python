# rasp 18_12_11 i2c_light, temp_humi sensor
# i2c device address: 0x23 (0010 0011)
# 확인 sudo i2c detect -y 1
# address : 0x40
# channel : 1

import smbus2 as smbus
import time

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
    
    print('lx :', result, 'humi :', humi, 'temp :', temp)

    time.sleep(0.5)