# Description: Olx web scraper
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from oferta import Oferta
from functions import get_page_source

class OlxOferta(Oferta):
   # Gaseste id-ul ofertei curente
   def find_id(self):
      # Faceți o cerere HTTP la pagina produsului
      product_response = requests.get(self.url)

      if product_response.status_code != 200:
         print("Cererea HTTP pentru produs a eșuat, url produs:" + self.url)
         return      
      product_html = product_response.text
      product_soup = BeautifulSoup(product_html, 'html.parser')

      # Extrage elementul span cu ID-ul produsului
      id_element = product_soup.find('span', class_="css-12hdxwj") # css-12hdxwj er34gjf0

      if id_element:
         # Extragem textul din element și eliminăm "ID: " pentru a obține numărul
         self.id =  id_element.get_text().replace("ID: ", "")
         return
      
      print("Elemetul cu ID-ul nu a fost gasit in pagina produsului: ", self.url)
      return 
   
   # Gaseste numarul de vizualizari al ofertei curente
   def find_views(self):
      # Inițializați un driver Selenium (asigurați-vă că aveți instalat Selenium și un driver de browser, de exemplu, pentru Edge)
      driver = webdriver.Edge()

      # Deschideți pagina web
      driver.get(self.url)

      # Așteptați să se încarce conținutul (puteți ajusta timpul de așteptare la nevoie)
      driver.implicitly_wait(10) # seconds

      # click pe butonul de acceptare a cookie-urilor
      driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()

      # Găsiți elementul care conține numărul de vizualizări (utilizati selectorul potrivit)
      vizualizari_element = driver.find_element(By.XPATH,"//*[contains(text(), 'Vizualizări')]")

      if not vizualizari_element:
         driver.quit() # Închideți browser-ul
         return 
      
      # Obțineți textul din element
      vizualizari_text = vizualizari_element.text

      # Utilizați o expresie regulată pentru a extrage numărul
      match = re.search(r'\d+', vizualizari_text)

      if match:
         self.views = match.group()
      
      driver.quit() # Închideți browser-ul
      return

   # Gaseste url-urile pozelor ofertei curente
   def find_photo_urls(self):
      # Extrage codul sursa al paginii dupa ce a fost incarcat un anumit element, folosind Selenium
      self.page_source = get_page_source(self.url, "div.swiper-zoom-container")
      product_soup = BeautifulSoup(self.page_source, "html.parser")

      # Extrage elementele div cu pozele produsului
      photo_elements = product_soup.find_all("div", class_="swiper-zoom-container")

      # Extrage url-urile pozelor din elementele gasite
      for photo_element in photo_elements:
         # Extrage url-ul pozei din div > img > src
         photo_url = photo_element.find("img")["src"]
         self.photo_urls.append(photo_url)

   # Completeaza campurile ofertei curente
   def complete_fields(self):
      self.find_id()
      try:
        self.find_views()
      except:
         self.views = "0"
      self.find_photo_urls()

class Olx:
   # Returneaza o lista de oferte
   def get_oferte(url, limit = 5):
      oferte = []

      # Faceti o cerere HTTP la pagina de cautare
      response = requests.get(url)

      # Verificam daca cererea a fost reusita
      if response.status_code != 200:
         print("Cererea HTTP a esuat.")
         return None

      # Parsati HTML-ul folosind BeautifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')

      # Extragem url-urile
      # Găsiți toate elementele care conțin informații despre produse
      product_elements = soup.find_all('div', class_='css-1sw7q4x')
      for product_element in product_elements[:limit+1]: # {0, limit - 1}
         # Găsiți elementul <a> care conține legătura către produs
         a_element = product_element.find('a', class_='css-rc5s2u')
         if a_element:
            url_url = "https://www.olx.ro" + a_element['href']
            oferte.append( OlxOferta(url=url_url))
         
      # Extragem preturile
      # Gasiti elementele <p> care contine pretul
      i = 0
      price_elements = soup.find_all('p', class_='css-10b0gli er34gjf0')
      for price_element in price_elements[:len(oferte)]: 
         # Extrageti textul din elementul gasit
         price_text = price_element.get_text()
         match = re.search(r'\d+', price_text)
         if match:
            oferte[i].pret = match.group()
            i+=1
         else:
            print("Nu s-a putut extrage pretul produsului din textul: " + price_text)

      return oferte   

