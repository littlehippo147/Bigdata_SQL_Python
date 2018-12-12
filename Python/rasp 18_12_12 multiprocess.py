# Thread와 Process
# 쓰레드(Thread) : 작업 실행의 단위
# 프로세스(Process) : Task, 실행중인 프로그램, 여러 쓰레드를 가질 수 있음
#                    프로세스는 다른 프로세스와 독립된 고유한 자원을 갖는다.

# multiprocess.py

from multiprocessing import Process
import time

# Process
def myprocess():
    cnt = 0
    while True:
        print('myprocess :', cnt)
        cnt += 1
        time.sleep(1)

p_list = [] # 자식 process list
p = Process(target = myprocess, args = ()) # 자식 process 생성
p.start()
p_list.append(p)

num = 0
for i in range(20): # main(부모) process 자식과 따로 진행
    print('main process', num)
    num += 1
    time.sleep(1)
    
p.terminate() # 자식 process 종료

for p in p_list:
    p.join() # 자식 process 종결 확인?

print('main process Exiting') # 자식 process 종료 확인 후 main process 종료

# 리눅스에서 프로세스 정보보기 : ps -aux