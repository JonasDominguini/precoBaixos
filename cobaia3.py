from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests
from bs4  import BeautifulSoup
import pandas as pd
import schedule
import time

#Angeloni Monster
def energetico():

        lista_cerveja_lata = []

        response = requests.get('https://www.angeloni.com.br/super/busca?Nrpp=12&Ntt=monster')                        
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        cervejas = site.findAll('div', attrs={'class':'box-produto p-relative'})

        for cerveja in cervejas:
            
            produto = cerveja.find('h2', attrs={'class':'box-produto__desc-prod text-center'})
            valor_real = cerveja.find('span',attrs={'class':'box-produto__preco__valor'})
            valor_centavos = cerveja.find('span',attrs={'class':'box-produto__preco__centavos'})

            #Limpeza
            produto_refinado = produto.text.strip().rstrip('\n').lstrip('\n')        
            valor_real_refinado = valor_real.split()
            valor_centavos_refinado = valor_centavos.split()

            

        


            lista_cerveja_lata.append([produto_refinado , '  Valor a vista:  R$ '+ valor_real_refinado + valor_centavos_refinado])

        ceva = pd.DataFrame(lista_cerveja_lata, columns=[ 'Produto','Preco'])
        ceva.to_csv('angeloni/energetico/monsterLataAngeloni.csv', index=False)   

        df = pd.read_csv("angeloni/energetico/monsterLataAngeloni.csv")
        Amonster473 = df[df.Produto=="Energético Monster Energy Lata 473ml"]
        ceval1 = pd.DataFrame(Amonster473, columns=['Produto','Preco'])
        ceval1.to_csv('angeloni/cerveja/monsterAngeloni.csv', index=False)    

        print('opa')
                    
schedule.every(5).seconds.do(energetico)    
while 1:
    schedule.run_pending()
    time.sleep(1)