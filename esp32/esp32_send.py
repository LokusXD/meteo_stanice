import network
import machine
import time
import random
import math
import urequests
import json
import dht

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Redmi Note 9', '1111111111')
while not wlan.isconnected():
    pass
print('Connection successful')
print(wlan.ifconfig())
sensor = dht.DHT11(machine.Pin(4))

def post(temp, hum):
    
    # Set the URL and data for the POST request
    url = 'http://192.168.9.169/api/post_data'
    data = {'temperature': temp, 'humidity': hum}
    json_data = json.dumps(data)

    # Send the POST request
    response = urequests.post(url, data=json_data, headers={"Content-Type": "application/json"})

    # Print the response status code and text
    if response.status_code != 200:
        print("pyco")

    # Close the response
    response.close()

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    json_data = {'temperature': temp, 'humidity': hum}
    print(json_data)
    try:
        post(temp, hum)
    except:
        print("lol nefunguje xd posílání klíčenky")
    time.sleep(5)

