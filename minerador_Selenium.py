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

        Giassi_Skol350 = df[df.Produto=="Cerveja Pilsen Skol Lata 350ml"]

        Giassi_Amstel350 = df[df.Produto=="Cerveja Lager Puro Malte Amstel Lata 350ml"]
        cerveja_Giassi_Amstel = pd.DataFrame(Giassi_Amstel350, columns=['Produto','Preco'])
        cerveja_Giassi_Amstel.to_csv('giassi/cerveja/amstel350LataGiassi.csv', index=False)

        Giassi_AntarticaSub350 = df[df.Produto=="Cerveja Pilsen Antarctica Subzero Lata 350ml"]
        cerveja_Giassi_AntarticaSub350 = pd.DataFrame(Giassi_AntarticaSub350, columns=['Produto','Preco'])
        cerveja_Giassi_AntarticaSub350.to_csv('giassi/cerveja/antarticaSub350LataGiassi.csv', index=False)

        Giassi_Budweiser350 = df[df.Produto=="Cerveja Lager Budweiser Lata 350ml"]
        cerveja_Giassi_Budweiser350 = pd.DataFrame(Giassi_Budweiser350, columns=['Produto','Preco'])
        cerveja_Giassi_Budweiser350.to_csv('giassi/cerveja/Budweiser350LataGiassi.csv', index=False)

        Giassi_heniken473 = df[df.Produto=="Cerveja Lager Premium Puro Malte Heineken Lata 473ml"]
        cerveja_Giassi_heniken473 = pd.DataFrame(Giassi_heniken473, columns=['Produto','Preco'])
        cerveja_Giassi_heniken473.to_csv('giassi/cerveja/heniken473LataGiassi.csv', index=False)

        Giassi_ZeroHeineken350 = df[df.Produto=="Cerveja Lager Premium Puro Malte Zero Álcool Heineken Lata 350ml"]
        cerveja_Giassi_ZeroHeineken350 = pd.DataFrame(Giassi_ZeroHeineken350, columns=['Produto','Preco'])
        cerveja_Giassi_ZeroHeineken350.to_csv('giassi/cerveja/ZeroHeineken350LataGiassi.csv', index=False)

        Giassi_antartica350 = df[df.Produto=="Cerveja Pilsen Antarctica Original Lata 350ml"]
        cerveja_Giassi_antartica350 = pd.DataFrame(Giassi_antartica350, columns=['Produto','Preco'])
        cerveja_Giassi_antartica350.to_csv('giassi/cerveja/antartica350LataGiassi.csv', index=False)    

        Giassi_PilsnerBra350 = df[df.Produto=="Cerveja Pilsner Duplo Malte Brahma Lata 350ml"]
        cerveja_Giassi_PilsnerBra350 = pd.DataFrame(Giassi_antartica350, columns=['Produto','Preco'])
        cerveja_Giassi_PilsnerBra350.to_csv('giassi/cerveja/PilsnerBra350LataGiassi.csv', index=False)  

        Giassi_Amstel_269_Sem_Gluten = df[df.Produto=="Cerveja Lager Puro Malte sem Glúten Amstel Ultra Lata 269ml"]
        cerveja_Giassi_Amstel_269_Sem_Gluten = pd.DataFrame(Giassi_Amstel_269_Sem_Gluten, columns=['Produto','Preco'])
        cerveja_Giassi_Amstel_269_Sem_Gluten.to_csv('giassi/cerveja/Amstel_269_Sem_GlutenLataGiassi.csv', index=False)

        Giassi_TherezopolisGold350 = df[df.Produto=="Cerveja Lager Puro Malte Gold Therezópolis Lata 350ml"]
        cerveja_Giassi_TherezopolisGold350 = pd.DataFrame(Giassi_TherezopolisGold350, columns=['Produto','Preco'])
        cerveja_Giassi_TherezopolisGold350.to_csv('giassi/cerveja/TherezopolisGold350LataGiassi.csv', index=False)

        Giassi_Baly350 = df[df.Produto=="Cerveja Pilsen Puro Malte Baly Lata 350ml"]
        cerveja_Giassi_Baly350 = pd.DataFrame(Giassi_Baly350, columns=['Produto','Preco'])
        cerveja_Giassi_Baly350.to_csv('giassi/cerveja/Baly350LataGiassi.csv', index=False) 

        Giassi_Bohemia350 = df[df.Produto=="Cerveja Lager Puro Malte Bohemia Lata 350ml"]
        cerveja_Giassi_Bohemia350 = pd.DataFrame(Giassi_Bohemia350, columns=['Produto','Preco'])
        cerveja_Giassi_Bohemia350.to_csv('giassi/cerveja/Bohemia350LataGiassi.csv', index=False)  

        Giassi_Dado350 = df[df.Produto=="Cerveja Lager Puro Malte Dado Bier Lata 350ml"]
        cerveja_Giassi_Dado350 = pd.DataFrame(Giassi_Dado350, columns=['Produto','Preco'])
        cerveja_Giassi_Dado350.to_csv('giassi/cerveja/Dado350LataGiassi.csv', index=False) 

        Giassi_Opa350 = df[df.Produto=="Cerveja Pilsen Puro Malte Opa Bier Lata 350ml"]
        cerveja_Giassi_Opa350 = pd.DataFrame(Giassi_Opa350, columns=['Produto','Preco'])
        cerveja_Giassi_Opa350.to_csv('giassi/cerveja/Opa350LataGiassi.csv', index=False)

        Giassi_Hoegaarden330 = df[df.Produto=="Cerveja Witbier Hoegaarden Garrafa 330ml"]
        cerveja_Giassi_Hoegaarden330 = pd.DataFrame(Giassi_Hoegaarden330, columns=['Produto','Preco'])
        cerveja_Giassi_Hoegaarden330.to_csv('giassi/cerveja/Hoegaarden330LataGiassi.csv', index=False)

        Giassi_Lagunitas355 = df[df.Produto=="Cerveja IPA Lagunitas Garrafa 355ml"]
        cerveja_Giassi_Lagunitas355 = pd.DataFrame(Giassi_Lagunitas355, columns=['Produto','Preco'])
        cerveja_Giassi_Lagunitas355.to_csv('giassi/cerveja/Lagunitas355LataGiassi.csv', index=False)

        Giassi_Coruja350 = df[df.Produto=="Cerveja Lager Puro Malte Coruja Lata 350ml"]
        cerveja_Giassi_Coruja350 = pd.DataFrame(Giassi_Coruja350, columns=['Produto','Preco'])
        cerveja_Giassi_Coruja350.to_csv('giassi/cerveja/Coruja350LataGiassi.csv', index=False)

        Giassi_Stella350 = df[df.Produto=="Cerveja Lager Premium Stella Artois Lata 350ml"]
        cerveja_Giassi_Stella350 = pd.DataFrame(Giassi_Stella350, columns=['Produto','Preco'])
        cerveja_Giassi_Stella350.to_csv('giassi/cerveja/Stella350LataGiassi.csv', index=False)



        
        #Cerveja Lager Brahma Chopp Lata 350ml
        #parado na 34.
        
        #Cerveja Lager Brahma Chopp Lata 473ml
        

        cerveja_Giassi_Spaten = pd.DataFrame(Giassi_Spaten350, columns=['Produto','Preco'])
        cerveja_Giassi_Spaten.to_csv('giassi/cerveja/spatenLataGiassi.csv', index=False)

        cerveja_Giassi_heniken = pd.DataFrame(Giassi_heniken350, columns=['Produto','Preco'])
        cerveja_Giassi_heniken.to_csv('giassi/cerveja/henikenLataGiassi.csv', index=False)

        cerveja_Giassi_Eisenbahn = pd.DataFrame(Giassi_Eisenbahn350, columns=['Produto','Preco'])
        cerveja_Giassi_Eisenbahn.to_csv('giassi/cerveja/EisenbahnLataGiassi.csv', index=False)

        cerveja_Giassi_Eisenbahn = pd.DataFrame(Giassi_Eisenbahn350, columns=['Produto','Preco'])
        cerveja_Giassi_Eisenbahn.to_csv('giassi/cerveja/EisenbahnLataGiassi.csv', index=False)

        cerveja_Giassi_Skol350 = pd.DataFrame(Giassi_Skol350, columns=['Produto','Preco'])
        cerveja_Giassi_Skol350.to_csv('giassi/cerveja/brahma_Malzbier350LataGiassi.csv', index=False)

        webdriver.close()

        

