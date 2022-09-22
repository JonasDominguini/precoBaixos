from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

class Page:
        def __init__(self, driver):
                self.driver = driver

        lista_energetico_Althoff = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)

        webdriver.get('https://www.giassi.com.br/monster?_q=monster&map=ft')
        sleep(3)        

        content = webdriver.page_source
        site = bs(content, 'html.parser')  
        monster = site.find('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})

        produto = monster.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
        valor = monster.find('p', attrs={'class':'giassi-apps-custom-0-x-priceUnit'})
        
        print(produto.text)
        print(valor.text)

