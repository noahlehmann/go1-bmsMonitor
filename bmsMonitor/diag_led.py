import struct
import time

import paho.mqtt.client as mqtt


def alert_led(r, g, b):
    mqttc = mqtt.Client()

    mqttc.connect("192.168.123.161", 1883, 60)

    mqttc.loop_start()

    mqttc.publish("face_light/color", struct.pack('BBB', r, g, b), qos=2)
    time.sleep(1)
    mqttc.publish("face_light/color", struct.pack('BBB', 0, 0, 0), qos=2)
    time.sleep(1)
    mqttc.disconnect()


def const_led(r, g, b):
    mqttc = mqtt.Client()
    mqttc.connect("192.168.123.161", 1883, 60)
    mqttc.loop_start()

    mqttc.publish("face_light/color", struct.pack('BBB', r, g, b), qos=2)
    time.sleep(1)
    mqttc.disconnect()