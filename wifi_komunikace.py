import socket
import json

# Adresa a port pro naslouchání
host = '192.168.1.100'  # Adresa ESP32
port = 12345  # Port ESP32

# Vytvořit socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nastavit socket pro naslouchání na dané adrese a portu
server_socket.bind((host, port))
server_socket.listen(1)

# Přijmout připojení
client_socket, addr = server_socket.accept()

# Přijmout data
received_data = client_socket.recv(1024)

# Dekódovat JSON data
data = json.loads(received_data.decode())

# Zpracovat data podle potřeby
print(data)

# Uzavřít spojení
client_socket.close()
server_socket.close()