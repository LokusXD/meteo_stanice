Projekt METEO_STANICE

krátký popis fungování projektu: 
    - na počítači/serveru běží enginx web server
    - zároveň zde běží i python server (senosr_server - api.py)
    - na esp32 běží program který měří teplotu, vlhkost a posílá ji serveru

Nginx server:
    - zobrazuje html, zároveň umožňuje přesměrování příchozích dat na python server
    - taktéž umožňuje insertovat html soubor do jiného html souboru <--# include:"jméno_souboru.html"--> umožňuje tak mít jednotnou hlavičku, zápatí, navigační menu atd

Python server:
    -hsjsbj
