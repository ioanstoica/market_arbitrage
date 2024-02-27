import sys
from olx import Olx
from aliexpress import Aliexpress

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Url-ul paginii de cautare Aliexpress
url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="

# Argumente de intrare: url-ul unui proudus de pe olx
# Iesire: o oferta de pe aliexpress, prima gasita, in urma cautarii dupa prima poza a produsului de pe olx
def from_olx_get_aliexpress(url):
    # Extrage ofertele de pe pagina de cautare de la Olx
    oferte_olx = Olx.get_oferte(url, limit=1)
    oferta_olx = oferte_olx[0]
    oferta_olx.complete_fields()

    photo_url = oferta_olx.photo_urls[0]
    oferta_aliexpress = Aliexpress.get_oferte(url_aliseeks + photo_url, limit=1)[0]
    oferta_aliexpress.complete_fields()

    return oferta_aliexpress

product_name = "samsung-s20"

url = "https://www.olx.ro/oferte/q-" + product_name + "/?search[filter_float_price%3Ato]=1000"

print(url)

from_olx_get_aliexpress(url).save_csv("test.csv")