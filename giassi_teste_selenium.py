from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

class Page:
        def __init__(self, driver):
                self.driver = driver

        lista_vinho_Giassi = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)

        webdriver.get('https://www.giassi.com.br/bebidas-alcoolicas/vinhos?page=6')
        sleep(3)        

        content = webdriver.page_source
        site = bs(content, 'html.parser')  
        print('chegou em parsear')
      
        vinhos_Giassi = site.findAll('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})
        for vinho_Giassi in vinhos_Giassi:

                print('chegou em for')                
                produto_Giassi = vinho_Giassi.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
                valor_normal_Giassi = vinho_Giassi.find('p',attrs={'class':"giassi-apps-custom-0-x-priceUnit"})

                print(produto_Giassi)
                print(valor_normal_Giassi),

                print('chegou em listarr')

                produto_final = produto_Giassi.text.strip().rstrip('\n').lstrip('\n')  
                valor_final = valor_normal_Giassi.text.strip().rstrip('\n').lstrip('\n')

                lista_vinho_Giassi.append([produto_final, 'Valor: ' +  valor_final ])
        
        vinho = pd.DataFrame(lista_vinho_Giassi, columns=[ 'Produto','Preco'])
        vinho.to_csv('giassi/vinho/Giassi_vinho_garrafa.csv', index=False )

        df = pd.read_csv("giassi/vinho/vinhoGiassi.csv")
        Giassi_vinho_garrafa = df[df.Produto=="Vinho Chileno Tinto Meio Seco Concha y Toro Reservado Carménère Valle Central Garrafa 750ml"]

        vinho_reservado_Giassi = pd.DataFrame(Giassi_vinho_garrafa, columns=['Produto','Preco'])
        vinho_reservado_Giassi.to_csv('giassi/vinho/vinho_reservado_Giassi.csv', index=False)
        webdriver.close()

