
import telebot # Biblioteca para api do bot de fato, comandos e etc.

API_KEY = "5688522981:AAEh4I2k1KJFI_HbUKEgKKpslePAQRnVN9A"

bot = telebot.TeleBot(API_KEY)

#====================================================================================#
#Cerveja Bhrama: Primeiro comando handler abriga o comando que fica na interface do usuário,
# abaixo a função que consulta o csv, pegando a primeira linha do csv, depois façamos uma 
# limpeza do que vem do csv para ficar menos esquisito na resposta do bot.

@bot.message_handler(commands=["Bhrama"])
def Cerveja(mensagem):  
    print('alguém usou bhrama')
    
    with open('bistek/cerveja/bhramaBistek.csv') as fp:
        line = fp.readlines()    
        nw2 = (line[1])
        nw2b = ((nw2.replace('Â','')))

    with open('angeloni/cerveja/bhramaAngeloni.csv') as fp:
        line = fp.readlines()    
        nw1 = (line[1])      

    
    bot.send_message(mensagem.chat.id,' A Bhrama no supermercado Angeloni é') 
    bot.send_message(mensagem.chat.id, nw1)

    bot.send_message(mensagem.chat.id,' A Bhrama no supermercado Bistek é') 
    bot.send_message(mensagem.chat.id, nw2b)

#====================================================================================#
# Cerveja heineken:

@bot.message_handler(commands=["heineken"])
def Cerveja(mensagem):  

    print('alguém usou heineken')

    with open('angeloni/cerveja/henikenAngeloni.csv') as fp:
        line = fp.readlines()    
        nw4 = (line[1])

    with open('bistek/cerveja/henikenBistek.csv') as fp: 
        line = fp.readlines()    
        nw5 = (line[1])
        nw5b = ((nw5.replace('Â','')))  

    bot.send_message(mensagem.chat.id,' A Heineken no supermercado Angeloni:') 
    bot.send_message(mensagem.chat.id, nw4)
    
    bot.send_message(mensagem.chat.id,' A Heineken no supermercado Bistek:') 
    bot.send_message(mensagem.chat.id, nw5b)

#====================================================================================#
# Cerveja Eisenbahn

@bot.message_handler(commands=["Eisenbahn"])
def Cerveja(mensagem):   

    print('alguém usou Eisenbahn')
    
    with open('angeloni/cerveja/EisenbahnAngeloni.csv') as fp:
        line = fp.readlines()    
        nw6 = (line[1])

    with open('bistek/cerveja/EisenbahnBistek.csv') as fp: 
        line = fp.readlines()    
        nw7 = (line[1])
        nw7b = ((nw7.replace('Â','')))
     
    bot.send_message(mensagem.chat.id,' A Eisenbahn no supermercado Angeloni:') 
    bot.send_message(mensagem.chat.id, nw6)
    
    bot.send_message(mensagem.chat.id,' A Eisenbahn no supermercado Bistek:') 
    bot.send_message(mensagem.chat.id, nw7b)



#====================================================================================#
#Monster energético

@bot.message_handler(commands=["Monster"])
def Monster(mensagem): 

    print('alguém usou Monster')

    with open('monsterBistek.csv') as fp: 
        line = fp.readlines()    
        nw9 = (line[1])
        nw9b = ((nw9.replace('Â','')))
        nw9c = ((nw9b))    

    with open('monsterAngeloni.csv') as fp:
        line = fp.readlines()    
        nw8 = (line[1]) 


    bot.send_message(mensagem.chat.id,' Supermercado Angeloni:') 
    bot.send_message(mensagem.chat.id, nw8)
    
    bot.send_message(mensagem.chat.id,' Supermercado Bistek:') 
    bot.send_message(mensagem.chat.id, nw9c)

#====================================================================================#

#Menu do bot.
def verificar(mesagem):    
        return True 
@bot.message_handler(func=verificar)
def responder (mensagem):
    texto = """
    Escolha  uma opção abaixo para continuar( Clique no item):

        /Monster  Preço do energético Monster 473ml:

        /Bhrama   Preço da cerveja lata 350ml em cada mercado: 

        /heineken Preço  cerveja lata 350ml em cada mercado: 

        /Eisenbahn Preço  cerveja lata 350ml em cada mercado:    

    Por favor selecione uma das opções pois qualquer outra resposta não irá funcionar.

    """
    bot.reply_to(mensagem, texto )
#'Olá aqui é o bot de notícias eSocial. Em processo de construção'

bot.polling()

while True: # Don't end the main thread.
    pass
