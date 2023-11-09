# Plecand de la url-ul imaginii, putem obtine detalii despre ofertele de pe aliexpress care contin aceasta imagine. (titlu, pret, url)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import aliexpress

# Setăm codificarea consolei la UTF-8
sys.stdout.reconfigure(encoding="utf-8")




