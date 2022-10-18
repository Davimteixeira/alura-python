import forca
import jogo_de_adivinhação6
print('---------------------------------')
print('-------escolha seu jogo----------')
print('---------------------------------')


print("(1) forca (2) adivinhaçhão")

jogo = int(input("qual o jogo ?"))

if(jogo == 1):
    print('jogando forca')
elif(jogo == 2):
    print('jogando adivinhação')