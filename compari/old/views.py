from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import re

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Inițializați un driver Selenium (asigurați-vă că aveți instalat Selenium și un driver de browser, de exemplu, pentru Chrome)
driver = webdriver.Chrome()

def get_views(link):
   # Deschideți pagina web
   driver.get(link)

   # Așteptați să se încarce conținutul (puteți ajusta timpul de așteptare la nevoie)
   driver.implicitly_wait(10) # seconds

   # click pe butonul de acceptare a cookie-urilor
   driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()

   # Gasiti elementul cu id-ul
   id = driver.find_element(By.CSS_SELECTOR, ".css-12hdxwj").text
   print(id)

   # Găsiți elementul care conține numărul de vizualizări (utilizati selectorul potrivit)
   vizualizari_element = driver.find_element(By.XPATH,"//*[contains(text(), 'Vizualizări')]")

   if not vizualizari_element:
      # Închideți browser-ul
      driver.quit()
      return -1
   
   # Obțineți textul din element
   vizualizari_text = vizualizari_element.text

   # Procesați numărul de vizualizări după cum doriți
   print("Număr de vizualizări:", vizualizari_text)

   # Utilizați o expresie regulată pentru a extrage numărul
   match = re.search(r'\d+', vizualizari_text)

   if match:
      # Închideți browser-ul
      driver.quit()
      return match.group()
   

   # Închideți browser-ul
   driver.quit()
   return -1


print(get_views("https://www.olx.ro/d/oferta/iphone-11-pro-64gb-bateria-85-global-amanet-crangasi-51499-IDhHHRl.html?reason=ip%7Clister"))