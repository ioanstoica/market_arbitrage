# Description: Other functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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