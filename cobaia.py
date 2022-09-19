from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests
from bs4  import BeautifulSoup
import pandas as pd
import schedule
import time


def tota():
        lista_cerveja_lata_Bistek = []
        print('1 etapa')

        response = requests.get('https://loja10.bistek.com.br/catalogsearch/result/?q=monster')

                
        content = response.content

        site_Bistek = BeautifulSoup(content, 'html.parser')

        cervejas_Bistek = site_Bistek.findAll('div', attrs={'class':"product-item-info"})

        for cerveja_Bistek in cervejas_Bistek:
              
                produto_Bistek = cerveja_Bistek.find('strong', attrs={'class':'product name product-item-name'})
                valo_normal_bistek = cerveja_Bistek.find('span',attrs={'class':"price"})
                valor_Bistek = cerveja_Bistek.find('span',attrs={'class':"special-price"})
                valor_amigo_bistek = cerveja_Bistek.find('span',attrs={'class':"price-clube-bistek price"})   

                if ():
                                        
                        # Limpeza do valor preço a vista bistek:
                        valor_bistekBruto = valor_Bistek.text.strip().rstrip('\n').lstrip('\n').split()
                        valor_bistekRefinado = valor_bistekBruto[2 : 4]
                        valor_bistekFinal = (' '.join(valor_bistekRefinado))
                        
                        # limpeza do valor amigo bistek:
                        valor_clube_Bistek_bruto = valor_amigo_bistek.text.strip().rstrip('\n').lstrip('\n')
                        valor_clube_Bistek_refinado = valor_clube_Bistek_bruto

                        lista_cerveja_lata_Bistek.append([produto_Bistek.text.strip().rstrip('\n').lstrip('\n') ,'   Valor a vista ' + valor_bistekFinal + '  Clube bistek '+ valor_clube_Bistek_refinado ]) 
                        ceva = pd.DataFrame(lista_cerveja_lata_Bistek, columns=[ 'Produto','Preco'])
                        ceva.to_csv('bistek/energetico/monsterLataBistek.csv', index=False ) 
                else:
                                               
                        # Limpeza do valor normal de prateleira:
                        valo_normal_bistek_bruto = valo_normal_bistek.text.strip().rstrip('\n').lstrip('\n')
                        valo_normal_bistek_refinado = valo_normal_bistek_bruto  
                        lista_cerveja_lata_Bistek.append([produto_Bistek.text.strip().rstrip('\n').lstrip('\n') ,'   Valor a vista ' + valo_normal_bistek_refinado + '  Clube bistek '+ 'Indisponivel' ]) 
                        ceva = pd.DataFrame(lista_cerveja_lata_Bistek, columns=[ 'Produto','Preco'])
                        ceva.to_csv('bistek/energetico/monsterLataBistek.csv', index=False ) 
        

        df_Bistek = pd.read_csv("bistek/energetico/monsterLatabistek.csv")
        Bmonster473 = df_Bistek[df_Bistek.Produto=="Energético Monster Green 473ml"]
        ceval4 = pd.DataFrame(Bmonster473, columns=['Produto', 'Preco'])
        ceval4.to_csv('bistek/energetico/monsterBistek.csv', index=False)

        print(ceval4) 
#======================================================================================================================#
#Angeloni Monster

        lista_cerveja_lata = []

        response = requests.get('https://www.angeloni.com.br/super/busca?Nrpp=12&Ntt=monster')

                        
        content = response.content

        site = BeautifulSoup(content, 'html.parser')

        cervejas = site.findAll('div', attrs={'class':'box-produto p-relative'})

        for cerveja in cervejas:
                produto = cerveja.find('h2', attrs={'class':'box-produto__desc-prod text-center'})
                valor_real = cerveja.find('span',attrs={'class':'box-produto__preco__valor'})
                valor_centavos = cerveja.find('span',attrs={'class':'box-produto__preco__centavos'})

                lista_cerveja_lata.append([produto.text , '  Valor a vista:  R$ '+ valor_real.text + valor_centavos.text])

                ceva = pd.DataFrame(lista_cerveja_lata, columns=[ 'Produto','Preco'])
                ceva.to_csv('monsterLataAngeloni.csv', index=False)

                print(produto.text) 
                print('Valor do produto: R$', valor_real.text,valor_centavos.text)
                print()
                df = pd.read_csv("monsterLataAngeloni.csv")
                Amonster473 = df[df.Produto=="Energético Monster Energy Lata 473ml"]                

                print(Amonster473)
                ceval1 = pd.DataFrame(Amonster473, columns=['Produto','Preco'])
                ceval1.to_csv('monsterAngeloni.csv', index=False)
                
schedule.every(10).seconds.do(tota)
while 1:
    schedule.run_pending()
    time.sleep(10)