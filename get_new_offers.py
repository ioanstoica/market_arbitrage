# Extragem primele oferte de pe pagina principala de OLX
from olx import Olx

url = "https://www.olx.ro/oferte/"

# Extrage ofertele de pe pagina de cautare de la Olx
oferte_olx = Olx.get_oferte(url, limit=15)

# Scriem url-urile ofertelor in fisierul urls.txt
with open("urls.txt", "a") as file:
    for oferta_olx in oferte_olx:
        file.write(oferta_olx.url + "\n")
