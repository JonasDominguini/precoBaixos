from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd


class PageAlthoffCerva:
        def __init__(self, driver):
                self.driver = driver

        lista_cerveja_Althoff = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)

        webdriver.get('https://emcasa.althoff.com.br/busca/cerveja')
        sleep(3)
        cidade = webdriver.find_element(By.CSS_SELECTOR, '#body > div.MuiDialog-root.dynamic-dialog.undefined.MuiModal-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.dynamic-dialog-content.hidden-scrollbar > div > div.stores-list > div:nth-child(1) > div:nth-child(1) > div.header')
        button_confirmar = webdriver.find_element(By.CSS_SELECTOR, '#body > div.MuiDialog-root.dynamic-dialog.undefined.MuiModal-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.modal-bottom-fixed > div > button')
        cidade.click()
        sleep(2)
        button_confirmar.click()
        sleep(2)

        content = webdriver.page_source
        site = bs(content, 'html.parser')
        sleep(1)
        webdriver.close()
        cervejas_Althoff = site.findAll('div', attrs={'class':"link-product"})
        for cerveja_Althoff in cervejas_Althoff:
                
                produto_Althoff = cerveja_Althoff.find('span', attrs={'class':'description-text'})
                valo_normal_Althoff = cerveja_Althoff.find('div',attrs={'class':"price-value"})

                produto_final = produto_Althoff.text.strip().rstrip('\n').lstrip('\n')  
                valor_final = valo_normal_Althoff.text.strip().rstrip('\n').lstrip('\n')

                lista_cerveja_Althoff.append([produto_final, 'Valor R$: ' +  valor_final ])
        
        cerveja = pd.DataFrame(lista_cerveja_Althoff, columns=[ 'Produto','Preco'])
        cerveja.to_csv('althoff/cerveja/cervejaLataAlthoff.csv', index=False )

        df = pd.read_csv("althoff/cerveja/cervejaLataAlthoff.csv")
        Althoff_cerveja473 = df[df.Produto=="Cerveja Campo Largo Com Vinho Red 500ml"]

        cerveja_Althoff = pd.DataFrame(Althoff_cerveja473, columns=['Produto','Preco'])
        cerveja_Althoff.to_csv('althoff/cerveja/lataAlthoff.csv', index=False)
        sleep(3)
        webdriver.close()

