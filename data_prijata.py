import serial
import json

# Otevřít sériovou komunikaci
ser = serial.Serial('/dev/ttyUSB0', 115200)  # Upravte podle vaší konfigurace

while ser.in_waiting:
    # Přijmout data
    received_data = ser.read_all()

    # Dekódovat JSON data
    data = json.loads(received_data)

    # Zpracovat data podle potřeby
    print(data)