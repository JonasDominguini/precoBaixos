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

        webdriver.get('https://emcasa.althoff.com.br/busca/monster')
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
        energeticos_Bistek = site.findAll('div', attrs={'class':"link-product"})
        for energetico_Bistek in energeticos_Bistek:
                
                produto_Althoff = energetico_Bistek.find('span', attrs={'class':'description-text'})
                valo_normal_Althoff = energetico_Bistek.find('div',attrs={'class':"price-value"})

                produto_final = produto_Althoff.text.strip().rstrip('\n').lstrip('\n')  
                valor_final = valo_normal_Althoff.text.strip().rstrip('\n').lstrip('\n')

                lista_energetico_Althoff.append([produto_final, 'Valor R$: ' +  valor_final ])
        
        energetico = pd.DataFrame(lista_energetico_Althoff, columns=[ 'Produto','Preco'])
        energetico.to_csv('althoff/energetico/energeticoLataAlthoff.csv', index=False )

        df = pd.read_csv("althoff/energetico/energeticoLataAlthoff.csv")
        Althoff_Energetico473 = df[df.Produto=="bebida energética monster green lata 473ml"]

        energetico_Althoff = pd.DataFrame(Althoff_Energetico473, columns=['Produto','Preco'])
        energetico_Althoff.to_csv('althoff/energetico/monsterAlthoff.csv', index=False)


