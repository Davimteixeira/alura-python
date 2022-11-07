import random

def jogar_adivinhacao():

  print('---------------------------------')
  print('bem vindo ao jogo de adivinhação')
  print('---------------------------------')

  numero_secreto = random.randrange(1,101) 
  total_de_tentativas = 0
  ontos = 1000

  print("qual o nivel de dificuldade ?")
  print("(1) fácil (2) médio (3) dificil")

  nivel = int(input("defina um nivel: "))

  if(nivel == 1):
    total_de_tentativas = 20
  elif(nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5

  for rodada in range(1, total_de_tentativas + 1):
    print(f"tentativa {rodada} de {total_de_tentativas}")
    chute_str = input('digite um numero entre 1 e 100: ')
    print('voce digitou', chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100")
        continue
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
         print(f"Você acertou e fez {pontos}")
         break
    else:
        if (maior):
           print("Você errou! O seu chute foi maior que o número secreto.")   
        elif (menor):
           print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    if (total_de_tentativas == rodada):
           print("FIM DE JOGO !!!!!")
    