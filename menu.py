import adivinhacao
import forca
print("selecione um jogo")

print("1 - adivinhação \n2 - forca")

escolha = int(input())

if(escolha == 1):
    adivinhacao.jogar()
elif(escolha == 2):
    forca.jogar()