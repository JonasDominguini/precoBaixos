from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests # biblioteca para pegar as requisições e respostas do site
from bs4  import BeautifulSoup # biblioteca que faz todo parsear ou tratamento do html
import pandas as pd # aonde criamos os csv, ou os dataframes que tanto falam do pandas
import schedule # tanto o time quanto isso, é para de acordo com o tempo estipulado para fazer a raspagem
import time

#=====================================================================================================================================================================#
        #Althoff Energético
        # Precisa de interação com a página, pois o mercado pede localização, é dose meus amigos.
def minerador():

    lista_energetico_lata_Althoff = []
       

    response = requests.get('https://emcasa.althoff.com.br/busca/monster')

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


schedule.every(20).seconds.do(minerador)
while 1:
    schedule.run_pending()
    time.sleep(1)