def jogar():
    import random

    #variaveis iniciais
    numero_s = random.randint(1, 100)
    vidas = 0
    pontos = 1000
    pontos_perdidos = 0

    

    apresentacao()
    #jogador escolhe o nivel
    while vidas == 0:
            
        print("Dificuldade:")
        print("1 Facil/ 2 Medio/ 3 Dificil")

        nivel = int(input("Escolha um nivel: "))

        if nivel == 1:
            vidas = 10
        elif nivel == 2:
            vidas = 5
        elif nivel == 3:
            vidas = 3
        else: 
            print("le direito porra \n")

    print(numero_s)

    #jogador entra de fato no jogo
    for i in range(0, vidas):
        print("*******************************")
        print(f"tentativa: {i + 1} de {vidas}")
        print(f"pontos: {pontos}")
        
        chute = int(input("Digite um numero de 1 a 100: "))
        
        #Verifica se o chute foi umnumero valido
        if(chute < 1) or (chute > 100):
            print("Digite um numero de 1 a 100")
            continue
        #Verificação se o jogador acertou ou não(retorno booleano)
        acertou = chute == numero_s
        maior = chute > numero_s
        menor = chute < numero_s

        
            
        print("voce digitou: ", chute)

        #avisa o jogador sobre o erro ou acerto
        if (acertou):
            print(f"você acertou e fez {pontos} pontos")
            break
        elif(maior):
            print("o numero é menor")
            pontos_perdidos = calcula(numero_s, chute)
        elif(menor):
            print("o numero é maior")
            pontos_perdidos = calcula(numero_s, chute)

        pontos = pontos - pontos_perdidos
        
        print("")


def apresentacao():
    print("*******************************")
    print("bem vido ao jogo da adivinhação")
    print("*******************************")
#função para calcular os pontos do jogador
def calcula(numero_s, chute):
    pontos_perdidos = abs(numero_s - chute)
    return pontos_perdidos

#ultima função
if(__name__ == "__main__"):
    jogar()