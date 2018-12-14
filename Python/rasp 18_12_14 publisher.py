import paho.mqtt.client as mqtt

# publish message
mqttc = mqtt.Client("python_pub")      # MQTT Client 오브젝트 생성
#mqttc.connect("test.mosquitto.org", 1883)    # MQTT 
mqttc.connect("localhost", 1883)    # iCORE-SDP Broker MQTT 서버 연결
# 'hello/world'  "Hello World!" 메세지 발생
mqttc.publish("hello/world", "I am Raspberry!! Hello World!")  
mqttc.loop(2)        # timeout = 2
