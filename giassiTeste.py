#import requests
from bs4  import BeautifulSoup
import pandas as pd
import schedule
import time
import requests

# Outra coisa sem resolver

response = requests.get('https://www.giassi.com.br/monster?_q=monster&map=ft')

                        
content = response.content

site = BeautifulSoup(content, 'html.parser')

monster = site.find('a', attrs={'class':'vtex-product-summary-2-x-clearLink h-100 flex flex-column'})

produto = monster.find('span', attrs={'class':'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'})
print(produto.text)
#vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body