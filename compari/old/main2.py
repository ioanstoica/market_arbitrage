# Clasa de oferte
# Extrage preturile, url-urile, id-urile si numarul de vizualizari
import requests
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding="utf-8")


# Clasa de oferte
class Oferta:
    def __init__(
        self,
        id="No id",
        titlu="No title",
        pret="No price",
        url="No url",
        views="No views",
    ):
        self.id = id
        self.titlu = titlu
        self.pret = pret
        self.url = url
        self.views = views

    def __str__(self):
        return (
            "ID: "
            + self.id
            + "\n"
            + "Titlu: "
            + self.titlu
            + "\n"
            + "Pret: "
            + self.pret
            + "\n"
            + "Url: "
            + self.url
            + "\n"
            "Vizualizari: " + self.views + "\n"
        )

    def csv_line(self):
        return (
            self.id
            + ","
            + self.titlu
            + ","
            + self.pret
            + ","
            + self.url
            + ","
            + self.views
            + "\n"
        )


# Returneaza id-ul produsului de la url-ul dat ca parametru
def get_id_element(url):
    # Faceți o cerere HTTP la pagina produsului
    product_response = requests.get(url)

    if product_response.status_code != 200:
        print("Cererea HTTP pentru produs a eșuat, url produs:" + url)
        return 0

    product_html = product_response.text
    product_soup = BeautifulSoup(product_html, "html.parser")

    # Extrage elementul span cu ID-ul produsului
    id_element = product_soup.find("span", class_="css-12hdxwj")  # css-12hdxwj er34gjf0

    if id_element:
        # Extragem textul din element și eliminăm "ID: " pentru a obține numărul
        product_id = id_element.get_text().replace("ID: ", "")
        return product_id
    else:
        print("Elemetul cu ID-ul nu a fost gasit in pagina produsului: ", url)
        return 0


# Returneaza o lista de oferte
def get_oferte(url, limit=5):
    oferte = []

    # Faceti o cerere HTTP la pagina de cautare
    response = requests.get(url)

    # Verificam daca cererea a fost reusita
    if response.status_code != 200:
        print("Cererea HTTP a esuat.")
        return None

    # Parsati HTML-ul folosind BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extragem url-urile
    # Găsiți toate elementele care conțin informații despre produse
    product_elements = soup.find_all("div", class_="css-1sw7q4x")
    for product_element in product_elements[: limit + 1]:  # {0, limit - 1}
        # Găsiți elementul <a> care conține legătura către produs
        a_element = product_element.find("a", class_="css-rc5s2u")
        if a_element:
            url_url = "https://www.olx.ro" + a_element["href"]
            oferte.append(Oferta(url=url_url))

    # Extragem preturile
    # Gasiti elementele <p> care contine pretul
    i = 0
    price_elements = soup.find_all("p", class_="css-10b0gli er34gjf0")
    for price_element in price_elements[: len(oferte)]:
        # Extrageti textul din elementul gasit
        price_text = price_element.get_text()
        oferte[i].pret = price_text
        i += 1

    return oferte


# Returneaza numarul de vizualizari al produsului de la url-ul dat ca parametru
def get_views(url):
    # Inițializați un driver Selenium (asigurați-vă că aveți instalat Selenium și un driver de browser, de exemplu, pentru Edge)
    driver = webdriver.Edge()

    # Deschideți pagina web
    driver.get(url)

    # Așteptați să se încarce conținutul (puteți ajusta timpul de așteptare la nevoie)
    driver.implicitly_wait(10)  # seconds

    # click pe butonul de acceptare a cookie-urilor
    driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()

    # Găsiți elementul care conține numărul de vizualizări (utilizati selectorul potrivit)
    vizualizari_element = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Vizualizări')]"
    )

    if not vizualizari_element:
        driver.quit()  # Închideți browser-ul
        return -1

    # Obțineți textul din element
    vizualizari_text = vizualizari_element.text

    # Utilizați o expresie regulată pentru a extrage numărul
    match = re.search(r"\d+", vizualizari_text)

    if match:
        driver.quit()  # Închideți browser-ul
        return match.group()

    driver.quit()  # Închideți browser-ul
    return -1


# URL-ul paginii de cautare OLX pentru "pubg-trigger"
url = "https://www.olx.ro/oferte/q-pubg-trigger/"

oferte = get_oferte(url, limit=2)
for oferta in oferte:
    oferta.id = get_id_element(oferta.url)
    try:
        oferta.views = get_views(oferta.url)
    except:
        print("Nu am putut extrage vizualizarile.")

for oferta in oferte:
    print(oferta)

with open("oferte.csv", "a", encoding="utf-8") as f:
    for oferta in oferte:
        f.write(oferta.csv_line())
