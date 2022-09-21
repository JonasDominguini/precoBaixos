from cgitb import text
from hashlib import new
from http.server import executable
#import imp
from certifi import contents
import requests # biblioteca para pegar as requisições e respostas do site
from bs4  import BeautifulSoup # biblioteca que faz todo parsear ou tratamento do html
import pandas as pd # aonde criamos os csv, ou os dataframes que tanto falam do pandas
import schedule # tanto o time quanto isso, é para de acordo com o tempo estipulado para fazer a raspagem
import time
#===========================================================#
# lá vem o selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver 

#=====================================================================================================================================================================#
        #Althoff Energético
        # Precisa de interação com a página, pois o mercado pede localização, é dose meus amigos.

chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)

sleep(2)
response = requests.get('https://emcasa.althoff.com.br/busca/monster')

webdriver.get('https://emcasa.althoff.com.br/busca/monster')
sleep(2)

cidade = webdriver.find_element(By.CSS_SELECTOR, '#body > div.MuiDialog-root.dynamic-dialog.undefined.MuiModal-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.dynamic-dialog-content.hidden-scrollbar > div > div.stores-list > div:nth-child(1) > div:nth-child(1) > div.header')
button_confirmar = webdriver.find_element(By.CSS_SELECTOR, '#body > div.MuiDialog-root.dynamic-dialog.undefined.MuiModal-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.modal-bottom-fixed > div > button')
cidade.click()
sleep(2)
button_confirmar.click()
sleep(2)
#lista_energetico_lata_Althoff = []       

#response = requests.get('https://emcasa.althoff.com.br/busca/monster')

print( 'oiii')

                
content = response.content

site_Bistek = BeautifulSoup(content, 'html.parser')
print(site_Bistek)

energeticos_Bistek = site_Bistek.findAll('div', attrs={'class':"link-product"})

for energetico_Bistek in energeticos_Bistek:
              
    produto_Althoff = energetico_Bistek.find('span', attrs={'class':'description-text'})
    valo_normal_Althoff = energetico_Bistek.find('div',attrs={'class':"price-value"}) 

    print(produto_Althoff)   
    print(valo_normal_Althoff)  

