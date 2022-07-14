import random

print("bem vido ao jogo de adivinhação")

numero_s = random.randint(1, 100)
vidas = 0
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
for i in range(0, vidas):
    print("*******************************")
    print(f"tentativa: {i + 1} de {vidas}")
    
    chute = int(input("Digite um numero de 1 a 100: "))
    
    
    if(chute < 1) or (chute > 100):
        print("Digite um numero de 1 a 100")
        continue

    acertou = chute == numero_s
    maior = chute > numero_s
    menor = chute < numero_s
    
    print("voce digitou: ", chute)

    if (acertou):
        print("você acertou")
        break
    elif(maior):
        print("o numero é menor")
    elif(menor):
        print("o numero é maior")
    
    print("")