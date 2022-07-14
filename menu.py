import jogo
import jogo2
print("selecione um jogo")

print("1 - adivinhação \n2 - forca")

escolha = int(input())

if(escolha == 1):
    jogo.jogar()
elif(escolha == 2):
    jogo2.jogar()