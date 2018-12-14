import paho.mqtt.client as mqtt

# client가 서버에 connect 응답을 받을때 호출되는 콜백 함수 
def on_connect(client, userdata, flags,rc):
  print ("Connected with result code " + str(rc))
  client.subscribe("hello/world")

# publisher한테 메시지를 subscribe 할 때 호출
def on_message(client, userdata, msg):
  print ("Topic: ", msg.topic + '\nMessage: ' + str(msg.payload))

client = mqtt.Client()        # MQTT Client 오브젝트 생성 
client.on_connect = on_connect     # on_connect callback 설정 
client.on_message = on_message   # on_message callback 설정

#client.connect("test.mosquitto.org", 1883, 60)   # MQTT 
client.connect("localhost", 1883, 60)   # iCORE-SDP Broker 서버 연결 

# 네트웍 트래픽 처리, 콜백 디스패치, 재접속 등을 수행하는 블로킹 함수
client.loop_forever()
