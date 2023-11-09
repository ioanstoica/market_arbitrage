# Description: Aliexpress web scraper
from bs4 import BeautifulSoup
from oferta import Oferta
from functions import get_page_source
import re
class AliexpresssOferta(Oferta):
    def complete_fields(self):
        self.find_titlu()
        self.find_pret()

    def find_pret(self):
        try:
            # Extrage codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
            if not self.page_source:
                self.page_source = get_page_source(self.url, "div.es--wrap--erdmPRe")
            product_soup = BeautifulSoup(self.page_source, "html.parser")

            # Extrage elementul div cu pretul produsului
            pret_element = product_soup.find("div", class_="es--wrap--erdmPRe")

            # Extrage prețul din elementul găsit
            pret = pret_element.text.strip()
            match = re.search(r'(\d[\d,.]*)', pret)

            if match:
                number_str = match.group(1)
                number_str = number_str.replace(",", "")
                self.pret = number_str
        except:
            print("Nu s-a putut extrage pretul produsului cu url-ul: " + self.url)
    
    def find_titlu(self):
        try:
            # Extrage codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
            if not self.page_source:
                self.page_source = get_page_source(self.url, "div.title--wrap--Ms9Zv4A")
            product_soup = BeautifulSoup(self.page_source, "html.parser")

            # Extrage elementul div cu titlul produsului
            titlu_element = product_soup.find("div", class_="title--wrap--Ms9Zv4A")

            # Extrage titlul din elementul găsit
            titlu = titlu_element.text.strip()
            self.titlu = titlu
        except:
            print("Nu s-a putut extrage titlul produsului cu url-ul: " + self.url)

class Aliexpress:
    # Returneaza o lista de oferte
    def get_oferte(url, limit=5):
        page_source = get_page_source(url, "a-image-search-product")
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
                oferte.append(AliexpresssOferta(url=url))

        return oferte

