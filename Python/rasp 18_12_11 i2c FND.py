# channel 1

import smbus2 as smbus
import time

addr = 0x20
config_port = 0x06
output_port = 0x02
# digits = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
digits = (0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6) 
# segment number = 1, 2, 3, 4, 5, 6
seg = (0x7E, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB)

bus = smbus.SMBus(1)
bus.write_word_data(addr, config_port, 0x0000) # 16 bits

for i in range(6):
    for j in range(9,-1,-1):
        out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
        bus.write_word_data(addr, output_port, out_disp) # 16 bits
        time.sleep(0.1)

time.sleep(1)
# 숫자들을 동시에 나오게 하는 방법은 없음
# Dynamic refresh를 이용해 빠르게 여러 자리의 숫자를 표시함
s = time.time()
e = time.time()
while e - s <= 6:
    for j in range(10):
        if e - s <= 1:
            for i in range(6):
                out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
                bus.write_word_data(addr, output_port, out_disp) # 16 bits
                time.sleep(0.005)
        elif e - s <= 2:
            for i in range(1,6):
                out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
                bus.write_word_data(addr, output_port, out_disp) # 16 bits
                time.sleep(0.005)
        elif e - s <= 3:
            for i in range(2,6):
                out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
                bus.write_word_data(addr, output_port, out_disp) # 16 bits
                time.sleep(0.005)    
        elif e - s <= 4:
            for i in range(3,6):
                out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
                bus.write_word_data(addr, output_port, out_disp) # 16 bits
                time.sleep(0.005)
        elif e - s <= 5:
            for i in range(4,6):
                out_disp = (digits[j]<<8) + seg[i] # 0xFC00 + 0x01 = 0xFC01
                bus.write_word_data(addr, output_port, out_disp) # 16 bits
                time.sleep(0.005)
        else:
            out_disp = (digits[j]<<8) + seg[5] # 0xFC00 + 0x01 = 0xFC01
            bus.write_word_data(addr, output_port, out_disp) # 16 bits
            time.sleep(0.005)
    e = time.time()

bus.write_word_data(addr, output_port, 0xFCFB)