# Verificam daca o oferta este profitabila, adica gasim o oferta similara pe Aliexpress care are pretul mai mic decat pretul ofertei de pe OLX
from olx import Olx, OlxOferta
from aliexpress import Aliexpress


# Verificam daca o oferta este profitabila, adica gasim o oferta similara pe Aliexpress care are pretul mai mic decat pretul ofertei de pe OLX, daca da, salvam oferta in fisierul oferte_profitabile.txt
def check_profitability(url_oferta_olx):
    url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="

    # Extragem oferta de pe OLX
    oferta_olx = OlxOferta(url=url_oferta_olx)
    oferta_olx.complete_fields()

    print("Am extras oferta de pe OLX: " + str(oferta_olx))

    # Cautam oferte similare pe Aliexpress
    oferte_aliexpress = Aliexpress.get_oferte(
        url_aliseeks + oferta_olx.photo_urls[0], limit=1
    )
    print(
        "Am gasit "
        + str(len(oferte_aliexpress))
        + " oferte similare pe Aliexpress pentru oferta cu id-ul "
        + oferta_olx.id
        + "."
    )

    # Extrage pretul unui produs
    for oferta_aliexpress in oferte_aliexpress:
        try:
            oferta_aliexpress.complete_fields()
        except Exception as e:
            # elimina oferta din lista
            oferte_aliexpress.remove(oferta_aliexpress)

    # Verificam daca oferta este profitabila
    if len(oferte_aliexpress) > 0:
        oferta_aliexpress = oferte_aliexpress[0]
        print("Am extras oferta de pe Aliexpress: " + str(oferta_aliexpress))
        if oferta_olx.price < oferta_aliexpress.price:
            print("Oferta de pe OLX este profitabila.")
            with open("oferte_profitabile.txt", "a", encoding="utf-8") as f:
                f.write(
                    str(
                        float(oferta_olx.price)
                        / (float(oferta_aliexpress.price) + 0.01)
                    )
                    + ", "
                    + oferta_olx.url
                    + ", "
                    + oferta_aliexpress.url
                    + "\n"
                )
        else:
            print("Oferta de pe OLX nu este profitabila.")
    else:
        print("Nu am gasit oferte similare pe Aliexpress.")


url_oferta_olx = "https://www.olx.ro/d/oferta/palton-dama-marimea-36-IDfLlmg.html"
check_profitability(url_oferta_olx)
