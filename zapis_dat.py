import json
import random
import time
from PyQt5 import QtWidgets
from matplotlib import pyplot as plt

def json_fille():
    # Definice dat
    x = random.randint(1,10)
    y = random.randint(1,10)
    t = random.randint(1,10)
    data = {
        "temperature": x,   # Příklad délky
        "humidity": y,     # Příklad úhlu
        "time": t
    }

    # Název souboru, do kterého chcete data uložit
    file_name = "data.json"

    # Otevřeme soubor v režimu 'w' (write) a zapíšeme do něj data
    with open(file_name, 'w') as f:
        json.dump(data, f)

    print("Data byla zapsána do JSON souboru.")

#while True:
#    json_fille()
#    time.sleep(10)
x = []    
y = []    
    
plt.plot(x,y)    
    
plt.title("teplota a vlhkost")    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
plt.show()    