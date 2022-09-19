from importlib.resources import contents
from tika import parser
from cgitb import text
from hashlib import new
#import imp
from certifi import contents
import requests # biblioteca para pegar as requisições e respostas do site
from bs4  import BeautifulSoup # biblioteca que faz todo parsear ou tratamento do html
import pandas as pd # aonde criamos os csv, ou os dataframes que tanto falam do pandas
import schedule # tanto o time quanto isso, é para de acordo com o tempo estipulado para fazer a raspagem
import time
listaceva = []
    #dados = parser.from_file('mmmrosso.pdf')
    #raw['content']
parsed_pdf = parser.from_file("fort.pdf") 
dados = parsed_pdf['content']  
print(dados ) 
print(type(dados.strip().rstrip('\n').lstrip('\n')))

listaceva.append([dados.strip()])
ceva = pd.DataFrame(listaceva, columns=[ 'contents'])

tabela1 = pd.DataFrame(ceva, columns=['contents'])


tabela1.to_csv('fort.csv' ) 