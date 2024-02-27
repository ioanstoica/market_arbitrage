import sys
from olx import Olx
from aliexpress import Aliexpress

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# URL-ul paginii de cautare OLX pentru "pubg-trigger"
url = "https://www.olx.ro/oferte/q-pubg-trigger/"

# Extrage ofertele de pe pagina de cautare de la Olx
oferte_olx = Olx.get_oferte(url, limit=1)
for oferta_olx in oferte_olx:
   try:
      oferta_olx.complete_fields()
   except Exception as e:
      # elimina oferta din lista
      oferte_olx.remove(oferta_olx)   
      print(e)
print("Am extras si completat " + str(len(oferte_olx)) + " oferte de pe OLX.")

# Filtram ofertele care au mai mult de 100 de vizualizari
oferte_vizualizate = []
for oferta_olx in oferte_olx:
   if int(oferta_olx.views) > 100:
      oferte_vizualizate.append(oferta_olx)
print("Am filtrat ofertele care au mai mult de 100 de vizualizari. Au ramas " + str(len(oferte_vizualizate)) + " oferte.")

url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="

# Cautam produse similare pe Aliexpress
for oferta_olx in oferte_vizualizate:
   print("Cautam oferte similare pe Aliexpress pentru oferta cu id-ul " + oferta_olx.id + "...")   
   oferte_aliexpress = []

   # Cautam dupa fiecare poza a ofertei
   for photo_url in oferta_olx.photo_urls:
      oferte_aliexpress += Aliexpress.get_oferte(url_aliseeks + photo_url, limit=1)
   print("Am gasit " + str(len(oferte_aliexpress)) + " oferte similare pe Aliexpress pentru oferta cu id-ul " + oferta_olx.id + ".")

   # Extrage pretul unui produs
   for oferta_aliexpress in oferte_aliexpress:
      try:
         oferta_aliexpress.complete_fields()
      except Exception as e:
         # elimina oferta din lista
         oferte_aliexpress.remove(oferta_aliexpress)   
         print(e)
   
   # Sortam ofertele dupa pret
   oferte_aliexpress.sort(key=lambda x: x.pret)
   print("Am sortat ofertele dupa pret.")

   with open("oferte.txt", "a", encoding="utf-8") as f:
      f.write("Pentru oferta de pe olx: \n")
      f.write(oferta_olx.__str__() + "\n")
      f.write("Am gasit ofertele de pe aliexpress: \n")
      # Afisam ofertele
      for oferta_aliexpress in oferte_aliexpress:
         f.write(oferta_aliexpress.__str__() + "\n")
         f.write("\n")
   
   with open("perechi.csv", "a", encoding="utf-8") as f:
      for oferta_aliexpress in oferte_aliexpress:
         f.write(oferta_olx.csv_line())
         f.write(oferta_aliexpress.csv_line())
         f.write("\n")

# for oferta in oferte:
#     oferta.save_csv("oferte.csv")

# url_poza = "https://frankfurt.apollo.olxcdn.com/v1/files/r7wwqdp3c9tm2-RO/image;s=1000x700"
# url = url_aliseeks + url_poza

# oferte = Aliexpress.get_oferte(url, 1)

# # Extrage pretul unui produs
# for oferta in oferte:
#     oferta.complete_fields()

# for oferta in oferte:
#     oferta.save_csv("aliexpress.csv")
