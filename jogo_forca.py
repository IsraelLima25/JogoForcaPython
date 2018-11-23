def iniciar_partida():    
    for position in range(0,len(palavra)):
        tab_jogo.append("_")        
        
def verificar_letra(palavra,letra):    
    tab_indice=[]    
    for position in range(0,len(palavra)):
        if palavra[position]==letra:
            tab_indice.append(position)                    
    return tab_indice

def alterar_espelho(lista,letra):

    for l in lista:
          tab_jogo[l]=letra   

def check_forca(qtd_erro):
    if (qtd_erro>2):        
        print("ENFORCADO!!!")
        print("------------------------------------")
        print("A palavra correta é " + str(palavra));
        print("------------------------------------")
        return True

def letra_repetida(letra):
    pr = str(palavras_repetidas)
    if(pr.find(letra)<0):
        return False
    else:
        return True    
    
    
palavra=input ("Digite uma palavra:")
print("------------------------------------")
tab_jogo=[]
palavras_repetidas = []
tentativas = 0
acertos = 0
erros = 0
fim=False
iniciar_partida()

while (fim == False):
    
    if(tentativas==0):
        print(tab_jogo)
        print("------------------------------------")
    
        
    letra = input("Digite uma letra:")
    print("------------------------------------")
    if letra_repetida(letra)== False:
        palavras_repetidas.append(letra)
        tentativas+=1
    else:
        print("Está letra já foi colocada")
        print("------------------------------------")        
        continue
    
    lista_de_letras = verificar_letra(palavra,letra)
    
    if(len(lista_de_letras)==0):
        erros+=1
        print("errou!!!")
        print("------------------------------------")
    else:
        acertos+=1
        print("Acertou!!")
        print("------------------------------------")
        
    print("Quantidade de Erros " + str(erros))
    print("------------------------------------")

    if (check_forca(erros)==True):
        print("Tentativas " + str(tentativas))
        fim=True

    if (acertos==len(palavra)):
        print("Final da Partida. Você venceu!!!")
        print("------------------------------------")
        print("A palavra correta é " + str(palavra));
        fim=True
        
    alterar_espelho(verificar_letra(palavra,letra),letra)    
    print(tab_jogo)
   
    
           
      
   












