# Plecand de la url-ul imaginii, putem obtine detalii despre ofertele de pe aliexpress care contin aceasta imagine. (titlu, pret, url)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding="utf-8")

# Obtine codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
def get_page_source(url, element_css_selector):
    # Inițializați un driver Selenium (asigurați-vă că aveți instalat Selenium și un driver de browser, de exemplu, pentru Edge)
    driver = webdriver.Edge()

    # Deschideți pagina web
    driver.get(url)

    # Așteaptă ca toate elementele să fie încărcate
    wait = WebDriverWait(driver, 10)  # Așteaptă până la 10 secunde
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, element_css_selector))
    )

    page_source = driver.page_source

    driver.quit()

    return page_source

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

    def set_pret(self):
        try:
            # Extrage codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
            page_source = get_page_source(self.url, "div.es--wrap--erdmPRe")
            product_soup = BeautifulSoup(page_source, "html.parser")

            # Extrage elementul div cu pretul produsului
            pret_element = product_soup.find("div", class_="es--wrap--erdmPRe")

            # Extrage prețul din elementul găsit
            pret = pret_element.text.strip()
            self.pret = pret
        except:
            print("Nu s-a putut extrage pretul produsului cu url-ul: " + self.url)
    
    def set_titlu(self):
        try:
            # Extrage codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
            page_source = get_page_source(self.url, "div.title--wrap--Ms9Zv4A")
            product_soup = BeautifulSoup(page_source, "html.parser")

            # Extrage elementul div cu titlul produsului
            titlu_element = product_soup.find("div", class_="title--wrap--Ms9Zv4A")

            # Extrage titlul din elementul găsit
            titlu = titlu_element.text.strip()
            self.titlu = titlu
        except:
            print("Nu s-a putut extrage titlul produsului cu url-ul: " + self.url)


# Returneaza o lista de oferte
def get_oferte(page_source, limit=5):
    oferte = []

    # Parsati HTML-ul folosind BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Extragem url-urile
    # Găsiți toate elementele care conțin informații despre produse
    product_elements = soup.find_all("a-image-search-product")

    for product_element in product_elements[:limit]:  # {0, limit - 1}
        # Găsiți elementul <a> care conține legătura către produs
        a_element = product_element.find("a")
        if a_element:
            url = a_element["href"]
            oferte.append(Oferta(url=url))

    return oferte


url_poza = (
    "https://frankfurt.apollo.olxcdn.com/v1/files/r7wwqdp3c9tm2-RO/image;s=1000x700"
)
url_aliseeks = "https://www.aliseeks.com/search/image?aref=ff-sbi&imageurl="
url = url_aliseeks + url_poza

page_source = get_page_source(url, "a-image-search-product")
oferte = get_oferte(page_source, 3)

# Extrage pretul unui produs
for oferta in oferte:
    oferta.set_pret()
    oferta.set_titlu()

with open ("aliexpress.csv", "a", encoding="utf-8") as f:
   for oferta in oferte:
      f.write(oferta.csv_line())
