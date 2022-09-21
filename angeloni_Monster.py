from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests
from bs4  import BeautifulSoup
import pandas as pd
import schedule
import time

# Isso aqui está muito ruim, quebra sempre não consegui resolver: AttributeError: 'NoneType' object has no attribute 'text'
        
#======================================================================================================================#
#Angeloni Monster
def minerador():
        lista_cerveja_lata = []

        response = requests.get('https://www.angeloni.com.br/super/busca?Nrpp=12&Ntt=monster')

                        
        content = response.content

        site = BeautifulSoup(content, 'html.parser')

        cervejas = site.findAll('div', attrs={'class':'box-produto p-relative'})

        for cerveja in cervejas:

                produto = cerveja.find('h2', attrs={'class':'box-produto__desc-prod text-center'})
                valor_real = cerveja.find('span',attrs={'class':'box-produto__preco__valor'})
                valor_centavos = cerveja.find('span',attrs={'class':'box-produto__preco__centavos'})

                lista_cerveja_lata.append([produto.text ,'  Valor a vista:  R$ '+ valor_real.text + valor_centavos.text])

                ceva = pd.DataFrame(lista_cerveja_lata, columns=[ 'Produto','Preco'])
                ceva.to_csv('angeloni/energetico/monsterLataAngeloni.csv', index=False)

                df_Angeloni = pd.read_csv("angeloni/energetico/monsterLataAngeloni.csv") 
                Amonster473 = df_Angeloni[df_Angeloni.Produto=="Energético Monster Energy Lata 473ml"]  

                energetico_Angeloni = pd.DataFrame(Amonster473, columns=['Produto','Preco'])
                energetico_Angeloni.to_csv('angeloni/energetico/monsterAngeloni.csv', index=False)

schedule.every(5).seconds.do(minerador)
while 1:
    schedule.run_pending()
    time.sleep(1)

