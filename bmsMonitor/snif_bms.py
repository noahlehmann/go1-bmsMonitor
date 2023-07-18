import struct
import paho.mqtt.client as mqtt

from diag_led import alert_led, const_led


def on_connect(client, userdata, flags, rc):
    client.subscribe("bms/state")


def on_message(client, userdata, msg):
    # print("Topic received-> " + msg.topic)
    # print(msg.payload)
    [ver0, ver1, status, soc, current, cycle, temp0, temp1, temp2, temp3, cellV0, cellV1, cellV2, cellV3, cellV4,
     cellV5, cellV6, cellV7, cellV8, cellV9] = struct.unpack('BBBBiHBBBBHHHHHHHHHH', msg.payload)
    # print("BMS version -> " + str(ver0) + "." + str(ver1))
    # print("BMS status  -> " + str(status))
    # print("BMS SOC     -> " + str(soc) + "%")
    # print("BMS Current -> " + str(current) + "mA")
    # print("BMS Cycles  -> " + str(cycle))
    # print("BMS BAT1    -> " + str(temp0) + u"\xb0" + "C")
    # print("BMS BAT2    -> " + str(temp1) + u"\xb0" + "C")
    # print("BMS MOS     -> " + str(temp2) + u"\xb0" + "C")
    # print("BMS RES     -> " + str(temp3) + u"\xb0" + "C")
    myCellVoltage = cellV0 + cellV1 + cellV2 + cellV3 + cellV4 + cellV5 + cellV6 + cellV7 + cellV8 + cellV9
    # print("BMS Voltage -> " + str(myCellVoltage) + "mV")
    # now make a decision to set an alarm
    if not check_bms_responding(msg.payload):
        const_led(10, 10, 0)
    elif 4 >= soc:
        alert_led(255, 0, 0)


def check_bms_responding(payload):
    # if payload only zeros, return false;
    return 0 != int.from_bytes(payload, byteorder='big')


# print("connecting mqtt client")
client = mqtt.Client("Stick Data")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.123.161", 1883, 60)
try:
    client.loop_forever()
except:
    client.disconnect()
