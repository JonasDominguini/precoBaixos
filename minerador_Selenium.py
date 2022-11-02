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
        sleep(3)

#======================================================================================================#
# Giassi energetico monster

class PageGiassi:
        def __init__(self, driver):
                self.driver = driver
        lista_energetico_Giassi = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)
        sleep(3) 
        webdriver.get('https://www.giassi.com.br/monster?_q=monster&map=ft')
        sleep(3)        

        content = webdriver.page_source
        site = bs(content, 'html.parser')  
      
        energeticos_Giassi = site.findAll('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})
        for energetico_Giassi in energeticos_Giassi:
                
                produto_Giassi = energetico_Giassi.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
                valo_normal_Giassi = energetico_Giassi.find('p',attrs={'class':"giassi-apps-custom-0-x-priceUnit"})

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

#======================================================================================================#
# Giassi cerveja

class PageGiassiCerveja:
        def __init__(self, driver):
                self.driver = driver


        lista_cerveja_Giassi = [] 

        chromedrive_path = 'C:\precoBaixoDesenv\chromedriver.exe'
        webdriver = webdriver.Chrome(executable_path=chromedrive_path)
        sleep(3) 
        webdriver.get('https://www.giassi.com.br/cerveja?_q=cerveja&map=ft')
        sleep(3)        

        content = webdriver.page_source
        site = bs(content, 'html.parser')  
      
        cervejas_Giassi = site.findAll('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})
        for cerveja_Giassi in cervejas_Giassi:
                
                produto_Giassi = cerveja_Giassi.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
                valo_normal_Giassi = cerveja_Giassi.find('p',attrs={'class':"giassi-apps-custom-0-x-priceUnit"})

                produto_final = produto_Giassi.text.strip().rstrip('\n').lstrip('\n')  
                valor_final = valo_normal_Giassi.text.strip().rstrip('\n').lstrip('\n')

                lista_cerveja_Giassi.append([produto_final, 'Valor: ' +  valor_final ])
        
        cerva1 = pd.DataFrame(lista_cerveja_Giassi, columns=[ 'Produto','Preco'])
        cerva1.to_csv('giassi/cerveja/cervejaLataGiassi.csv', index=False )

        df = pd.read_csv("giassi/cerveja/cervejaLataGiassi.csv")
        Giassi_Spaten350 = df[df.Produto=="Cerveja Munich Helles Puro Malte Spaten Lata 350ml"]
        Giassi_heniken350 = df[df.Produto=="Cerveja Lager Premium Puro Malte Heineken Lata 350ml"]
        Giassi_Eisenbahn350 = df[df.Produto=="Cerveja Pilsen Puro Malte Eisenbahn Lata 350ml"]

        Giassi_Skol350 = df[df.Produto=='Cerveja Skol Pilsen Lata 350ml'] 
        Giassi_Skol473 = df[df.Produto=="Cerveja Skol Pilsen Lata 473ml"]
        cerveja_Giassi_Spaten = pd.DataFrame(Giassi_Spaten350, columns=['Produto','Preco'])
        cerveja_Giassi_Spaten.to_csv('giassi/cerveja/spatenLataGiassi.csv', index=False)



        #Cerveja Caracu Escura 350ml Lata
        #Cerveja Brahma Malzbier 350ml Lata
        #Cerveja Brahma Zero 350ml Lata
        #Cerveja Antarctica Sub Zero Pilsen 473ml Lata
        #Cerveja Brahma Extra Lager Puro Malte 350ml Lata
        #Cerveja Antarctica Sub Zero Pilsen 350ml Lata
        #Cerveja Brahma Chopp Pilsen 473ml Lata
        #Cerveja Budweiser American Lager 473ml Lata
        #Cerveja Kaiser Pilsen Lata 473ml
        #Cerveja Stella Artois Puro Malte 350ml Lata
        #Cerveja Heineken Zero Lata 350ml 
        #Cerveja Kaiser Pilsen Lata 350ml
        #Cerveja Schornstein Ipa Lata 473ml
        #Cerveja Amstel Puro Malte Lata 473ml
        #Cerveja Heineken Premium Puro Malte Lata 473ml
        #Cerveja Eisenbahn American Ipa Puro Malte Lata 350ml
        #Cerveja Budweiser American Lager 350ml Lata
        #Cerveja Bohemia Puro Malte Lata 473ml
        #Cerveja Amstel Puro Malte Lata 350ml
        #Cerveja Eisenbahn Pale Ale Puro Malte Lata 350ml
        #Cerveja Baden Baden Ipa Lata 350ml
        #Cerveja Baden Baden Pilsen Cristal Lata 350ml
        #Cerveja Eisenbahn Pilsen Puro Malte Lata 350ml


        cerveja_Giassi_Spaten = pd.DataFrame(Giassi_Spaten350, columns=['Produto','Preco'])
        cerveja_Giassi_Spaten.to_csv('giassi/cerveja/spatenLataGiassi.csv', index=False)

        cerveja_Giassi_heniken = pd.DataFrame(Giassi_heniken350, columns=['Produto','Preco'])
        cerveja_Giassi_heniken.to_csv('giassi/cerveja/henikenLataGiassi.csv', index=False)

        cerveja_Giassi_Eisenbahn = pd.DataFrame(Giassi_Eisenbahn350, columns=['Produto','Preco'])
        cerveja_Giassi_Eisenbahn.to_csv('giassi/cerveja/EisenbahnLataGiassi.csv', index=False)

        cerveja_Giassi_Eisenbahn = pd.DataFrame(Giassi_Eisenbahn350, columns=['Produto','Preco'])
        cerveja_Giassi_Eisenbahn.to_csv('giassi/cerveja/EisenbahnLataGiassi.csv', index=False)

        webdriver.close()

        

