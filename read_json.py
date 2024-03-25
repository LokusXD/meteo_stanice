import serial
import json

serial_port = 'COM3'
baud_rate = 9600

try:
    ser = serial.Serial(serial_port, baud_rate)
    print("Sériový port otevřen.")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            
            try:
                json_data = json.loads(line)
                print("Přijatá data:", json_data)
            except json.JSONDecodeError:
                print("Chyba při dekódování JSON dat:", line)
except serial.SerialException:
    print("Nepodařilo se otevřít sériový port. Ujistěte se, že ESP32 je připojeno a správně nakonfigurováno.")
