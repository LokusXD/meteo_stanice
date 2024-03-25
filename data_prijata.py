import serial
import json

# Otevřít sériovou komunikaci
ser = serial.Serial('COM3', 9600)  # Upravte podle vaší konfigurace

# Přijmout data
received_data = ser.read_all()

# Dekódovat JSON data
data = json.loads(received_data)

# Zpracovat data podle potřeby
print(data)