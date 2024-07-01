import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


url = "https://books.toscrape.com/index.html"
driver.get(url)
time.sleep(5)

links = driver.find_elements(By.CLASS_NAME, 'product_pod')
lista = []

for s in links:
   lista.append(s.text)
print(lista)

data = {"Titulo": lista}

dados = pd.DataFrame(data)

dados.to_excel("data.xlsx")