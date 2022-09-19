from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests # biblioteca para pegar as requisições e respostas do site
from bs4  import BeautifulSoup # biblioteca que faz todo parsear ou tratamento do html
import pandas as pd # aonde criamos os csv, ou os dataframes que tanto falam do pandas
import schedule # tanto o time quanto isso, é para de acordo com o tempo estipulado para fazer a raspagem
import time

# minerador total
def minerador():

        lista_cerveja_lata = []

        response = requests.get('https://www.angeloni.com.br/super/busca?No=0&Nr=AND(product.store:14,product.siteId:super,prop.product.indexableSuper:1,NOT(dim.product.type:product-recipe))&Nrpp=48&Ntt=cerveja+lata')

                
        content = response.content

        site = BeautifulSoup(content, 'html.parser')

        cervejas = site.findAll('div', attrs={'class':'box-produto p-relative'})

        for cerveja in cervejas:
                produto = cerveja.find('h2', attrs={'class':'box-produto__desc-prod text-center'})
                valor_real = cerveja.find('span',attrs={'class':'box-produto__preco__valor'})
                valor_centavos = cerveja.find('span',attrs={'class':'box-produto__preco__centavos'})

                lista_cerveja_lata.append([produto.text , '  Valor a vista:  R$ '+ valor_real.text + valor_centavos.text])

        ceva = pd.DataFrame(lista_cerveja_lata, columns=[ 'Produto','Preco'])
        ceva.to_csv('angeloni/cerveja/cervejaLataAngeloni.csv')

        print(produto.text) 
        print('Valor do produto: R$', valor_real.text,valor_centavos.text)
        print()
        df = pd.read_csv("angeloni/cerveja/cervejaLataAngeloni.csv")
        AcervejaBhrama350 = df[df.Produto=="Cerveja Brahma Extra Lager Puro Malte 350ml Lata"]
        AcervejaSubZero350 = df[df.Produto=="Cerveja Antarctica Sub Zero Pilsen 350ml Lata"]
        AcervejaHeineken350 = df[df.Produto=="Cerveja Heineken Lata 350ml "]
        AcervejaStela350 = df[df.Produto=="Cerveja Stella Artois Puro Malte 350ml Lata"] 
        AcervejaEisenbahn350 = df[df.Produto=="Cerveja Eisenbahn Pilsen Puro Malte Lata 350ml"] 
        AcervejaBadenBaden350 = df[df.Produto=="Cerveja Baden Baden Witbier Lata 350ml"]#Spaten Puro Malte 350ml Lata
        AcervejaSpaten350 = df[df.Produto=="Spaten Puro Malte 350ml Lata "]

        print(AcervejaEisenbahn350)
        ceval1 = pd.DataFrame(AcervejaBhrama350, columns=['Produto','Preco'])
        ceval1.to_csv('angeloni/cerveja/bhramaAngeloni.csv', index=False)

        ceval2 = pd.DataFrame(AcervejaEisenbahn350, columns=['Produto','Preco'])
        ceval2.to_csv('angeloni/cerveja/EisenbahnAngeloni.csv', index=False)

        ceval3 = pd.DataFrame(AcervejaHeineken350, columns=['Produto','Preco'])
        ceval3.to_csv('angeloni/cerveja/henikenAngeloni.csv', index=False)

        #===================================================================================================#
        #Bistek supermecado

        lista_cerveja_lata_Bistek = []

        response = requests.get('https://loja10.bistek.com.br/catalogsearch/result/index/?product_list_dir=asc&product_list_order=name&q=cerveja+lata&product_list_limit=all')

                
        content = response.content

        site_Bistek = BeautifulSoup(content, 'html.parser')

        cervejas_Bistek = site_Bistek.findAll('div', attrs={'class':"product-item-info"})

        for cerveja_Bistek in cervejas_Bistek:

                produto_Bistek = cerveja_Bistek.find('strong', attrs={'class':'product name product-item-name'})
                valor_Bistek = cerveja_Bistek.find('span',attrs={'class':"price"})

                lista_cerveja_lata_Bistek.append([produto_Bistek.text.strip(), '  Valor a vista:  ' + valor_Bistek.text]) 

        ceva = pd.DataFrame(lista_cerveja_lata_Bistek, columns=[ 'Produto','Preco'])

        ceva.to_csv('bistek/cerveja/cervejaLataBistek.csv', index=False ) 

        df_Bistek = pd.read_csv("bistek/cerveja/cervejaLatabistek.csv")
        BcervejaBhrama350 = df_Bistek[df_Bistek.Produto=="Cerveja Brahma Extra Lager Lata 350ml"]
        #BcervejaSubZero350 = df_Bistek[df_Bistek.Produto=="Cerveja Antarctica Subzero Lata 350ml"]
        BcervejaHeineken350 = df_Bistek[df_Bistek.Produto=="Cerveja Heineken Lata 350ml"]
        #AcervejaStela350 = df_Bistek[df_Bistek.Produto=="Cerveja Stella Artois Puro Malte 350ml Lata"] 
        BcervejaEisenbahn350 = df_Bistek[df_Bistek.Produto=="Cerveja Eisenbahn Pilsen Lata 350ml"] 
        #AcervejaBadenBaden350 = df_Bistek[df_Bistek.Produto=="Cerveja Baden Baden Witbier Lata 350ml"]#Spaten Puro Malte 350ml Lata
        BcervejaSpaten350 = df_Bistek[df_Bistek.Produto=="Cerveja Spaten Puro Malte Lata 350ml"]


        ceval4 = pd.DataFrame(BcervejaBhrama350, columns=['Produto','Preco'])
        ceval4.to_csv('bistek/cerveja/bhramaBistek.csv', index=False)

        ceval5 = pd.DataFrame(BcervejaEisenbahn350, columns=['Produto','Preco'])
        ceval5.to_csv('bistek/cerveja/EisenbahnBistek.csv', index=False)

        ceval6 = pd.DataFrame(BcervejaHeineken350, columns=['Produto','Preco'])
        ceval6.to_csv('bistek/cerveja/henikenBistek.csv', index=False)
        
schedule.every(10).seconds.do(minerador)
while 1:
    schedule.run_pending()
    time.sleep(10)