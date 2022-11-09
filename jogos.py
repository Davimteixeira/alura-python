import forca
import jogo_de_adivinhação6
print('---------------------------------')
print('-------ESCOLHA SEU JOGO----------')
print('---------------------------------')


print("(1) forca (2) adivinhaçhão")

jogo = int(input("qual o jogo ? \n"))

if(jogo == 1):
    print('jogando forca')
    forca.jogar()
elif(jogo == 2):
    print('jogando adivinhação')
    jogo_de_adivinhação6.jogar_adivinhacao()