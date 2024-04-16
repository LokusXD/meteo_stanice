import json
import random
import time

def json_fille():
    # Definice dat
    x = random.randint(1,10)
    y = random.randint(1,10)
    data = {
        "length": x,   # Příklad délky
        "angle": y     # Příklad úhlu
    }

    # Název souboru, do kterého chcete data uložit
    file_name = "data.json"

    # Otevřeme soubor v režimu 'w' (write) a zapíšeme do něj data
    with open(file_name, 'w') as f:
        json.dump(data, f)

    print("Data byla zapsána do JSON souboru.")

while True:
    json_fille()
    time.sleep(10)