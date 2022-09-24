from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

class Page:
        def __init__(self, driver):
                self.driver = driver

        lista_energetico_Giassi = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)

        webdriver.get('https://www.giassi.com.br/monster?_q=monster&map=ft')
        sleep(3)        

        content = webdriver.page_source
        site = bs(content, 'html.parser')  
      
        energeticos_Giassi = site.findAll('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})
        for energetico_Giassi in energeticos_Giassi:
                
                produto_Giassi = energetico_Giassi.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
                valo_normal_Giassi = energetico_Giassi.find('p',attrs={'class':"giassi-apps-custom-0-x-priceUnit"})

                print(produto_Giassi)
                print(valo_normal_Giassi)

                produto_final = produto_Giassi.text.strip().rstrip('\n').lstrip('\n')  
                valor_final = valo_normal_Giassi.text.strip().rstrip('\n').lstrip('\n')

                lista_energetico_Giassi.append([produto_final, 'Valor: ' +  valor_final ])
        
        energetico = pd.DataFrame(lista_energetico_Giassi, columns=[ 'Produto','Preco'])
        energetico.to_csv('giassi/energetico/energeticoLataGiassi.csv', index=False )

        df = pd.read_csv("giassi/energetico/energeticoLataGiassi.csv")
        Giassi_Energetico473 = df[df.Produto=="Energético Monster Lata 473ml"]

        energetico_Giassi1 = pd.DataFrame(Giassi_Energetico473, columns=['Produto','Preco'])
        energetico_Giassi1.to_csv('giassi/energetico/monsterGiassi.csv', index=False)
        webdriver.close()

