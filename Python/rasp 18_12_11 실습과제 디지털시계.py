# i2c FND를 이용한 디지털 시계 
import smbus2 as smbus
import time

addr = 0x20
config_port = 0x06
output_port = 0x02

bus = smbus.SMBus(1)
bus.write_word_data(addr, config_port, 0x0000) # 16 bits

# digits = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
digits = (0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6)
# segment number = 1, 2, 3, 4, 5, 6
seg = (0x7E, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB)

def main():
    while True:
        # 현재 시간 string으로 가져오기
        cur_time = time.ctime()
        # time slicing
        hour, minute, second = cur_time[11:13], cur_time[14:16], cur_time[17:19]
        strtime = hour + minute + second
        # time display
        for i in range(6):
            num = int(strtime[i])
            display_fnd(num, i)
            time.sleep(0.003)

def display_fnd(num, i):
    out_disp = (digits[num]<<8) + seg[i] 
    bus.write_word_data(addr, output_port, out_disp)
    

# main 실행
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    bus.write_word_data(addr, output_port, 0)
    


