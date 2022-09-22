# precoBaixos
Projeto com objetivo de coletar preços de diversos mercados de criciuma em especial. Iniciando pela busca de Angeloni e bistek. 
Após conseguir destes dois os preços de cerveja e energeticos foi criado um chatbot para integrar os dados tratados a uma interface
que entregasse a usuário final as informações obtidas. O objetivo é coletar do maximo de mercados que possuam sites. Foi identificado
Giassi e Althoff com sites também para scraping, porém terá abordagens diferentes dos dois anteriores devido a particularidades do mesmos.
Nesse caso vimos que requests e BeatfulSoup não seriam suficientes. As duas citadas anteriormente são bibliotecas Python.
Para esses sites vamos utilizar o selenium pois com seu webdriver é possivel interagir com a página( no caso althoff informar localização,
e do giassi a renderização dos preços que vêm de um javascript).
Outros mercados apenas pegaremos os valores promocionais presentes nos encartes da semana de cada um ( mmm Rosso, Fort atacadista, Maxxi, Moniari).
Já que estes mercados não possuem sites com preço disponivel para consulta. Nesse caso utilizaremos a biblioteca TIKA do python que faz a leitura desses PDFs.
Depois no tratamento de dados faremos a busca de produtos que desejamos.
Todos os dados serão armazenados a principios em CSV. Mais a frente  haverá a mudança para um banco de dados decente. A principio é de fato fazer o chatbot e 
scripts de mineração funcionar.
