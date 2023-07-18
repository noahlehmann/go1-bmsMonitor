import struct
import time

import paho.mqtt.client as mqtt

from constants import HOSTNAME, PORT, TIMEOUT, FACE_LIGHT_TOPIC, QOS


def alert_led(r, g, b):
    mqttc = mqtt.Client()

    mqttc.connect(HOSTNAME, PORT, TIMEOUT)

    mqttc.loop_start()

    mqttc.publish(FACE_LIGHT_TOPIC, struct.pack('BBB', r, g, b), qos=QOS)
    time.sleep(1)
    mqttc.publish(FACE_LIGHT_TOPIC, struct.pack('BBB', 0, 0, 0), qos=QOS)
    time.sleep(1)
    mqttc.disconnect()


def const_led(r, g, b):
    mqttc = mqtt.Client()
    mqttc.connect(HOSTNAME, PORT, TIMEOUT)
    mqttc.loop_start()

    mqttc.publish(FACE_LIGHT_TOPIC, struct.pack('BBB', r, g, b), qos=QOS)
    time.sleep(1)
    mqttc.disconnect()
