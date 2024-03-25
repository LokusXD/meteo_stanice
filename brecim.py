import serial
import json

# Otevřít sériovou komunikaci
ser = serial.Serial('COM3', 115200)  # Změňte 'COM1' na odpovídající port na vašem počítači

# Přijmout data
received_data = ser.readline()

# Převést data z bajtového řetězce na řetězec a pak na slovník
decoded_data = received_data.decode('utf-8')
data_dict = json.loads(decoded_data)

# Uložit data do souboru
with open('data.json', 'w') as file:
    json.dump(data_dict, file)