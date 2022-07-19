
import random



def jogar():
    apresentacao()
    palavra_secreta = gera_palavra()
    

    letras_corretas = ["_" for letra in palavra_secreta]
    print(letras_corretas)
    enforcar = False
    acertou = False
    erros = 0
   
    

    while (not enforcar) and (not acertou):
        
       
        chute = input ("Digite uma letra: ")
        chute = chute.strip().lower()
        
        

        if len(chute) != 1:
            print("digite apenas uma letra")
            continue
        elif(chute in palavra_secreta):
            chute_correto(palavra_secreta,letras_corretas,chute)
            
        else:
            erros += 1
            desenha_forca(erros)

        enforcar = erros == 7
        acertou = "_" not in letras_corretas
        print(letras_corretas)
            
    imprime_final(acertou, palavra_secreta)



#funções
def apresentacao():
    print("*************************")
    print("bem vido ao jogo de forca")
    print("*************************")

def gera_palavra():
    
    arquivo = open("palavras.txt", "r")

    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())


    arquivo.close()
    
    numero  = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def chute_correto(palavra_secreta,letras_corretas,chute):
    index = 0
    for letra in palavra_secreta:
             
        if chute == letra:
                    
            letras_corretas[index] = letra
                           
        index += 1
        


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_final(acertou, palavra_secreta):
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Voce Perdeu!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        

#ultima funçã
if(__name__ == "__main__"):
    jogar()
