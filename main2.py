import sys
from olx import Olx
from aliexpress import Aliexpress

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# URL-ul paginii de cautare OLX pentru "pubg-trigger"
url = "https://www.olx.ro/oferte/q-pubg-trigger/"

# oferte = Olx.get_oferte(url, limit=1)
# for oferta in oferte:
#    try:
#       oferta.complete_fields()
#    except:
#       print("Nu am putut completa campurile unei oferte olx.")

# for oferta in oferte:
#     oferta.save_csv("oferte.csv")

url_poza = "https://frankfurt.apollo.olxcdn.com/v1/files/r7wwqdp3c9tm2-RO/image;s=1000x700"
url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="
url = url_aliseeks + url_poza

oferte = Aliexpress.get_oferte(url, 1)

# Extrage pretul unui produs
for oferta in oferte:
    oferta.complete_fields()

for oferta in oferte:
    oferta.save_csv("aliexpress.csv")

print(float(oferte[0].pret))
