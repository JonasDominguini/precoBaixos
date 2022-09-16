import pandas as pd



#df = pd.read_csv('cervejaLataAngeloni.csv').head()

df = pd.read_csv("cervejaLataAngeloni.csv")
AcervejaBhrama350 = df[df.Produto=="Cerveja Brahma Extra Lager Puro Malte 350ml Lata"]
AcervejaSubZero350 = df[df.Produto=="Cerveja Antarctica Sub Zero Pilsen 350ml Lata"]
AcervejaHeineken350 = df[df.Produto=="Cerveja Heineken Lata 350ml "]
AcervejaStela350 = df[df.Produto=="Cerveja Stella Artois Puro Malte 350ml Lata"] 
AcervejaEisenbahn350 = df[df.Produto=="Cerveja Eisenbahn Pilsen Puro Malte Lata 350ml"] 
AcervejaBadenBaden350 = df[df.Produto=="Cerveja Baden Baden Witbier Lata 350ml"]#Spaten Puro Malte 350ml Lata
AcervejaSpaten350 = df[df.Produto=="Spaten Puro Malte 350ml Lata"]

print(AcervejaBhrama350)
print()
print()
print(AcervejaBadenBaden350)
print()
print()
print(AcervejaSubZero350 )
print()
print()
print(AcervejaSpaten350)

print(AcervejaHeineken350)
print()

print(AcervejaStela350)
print()

print(AcervejaEisenbahn350)

