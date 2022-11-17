print('---------------------------------')
print('bem vindo ao jogo de adivinhação')
print('---------------------------------')

numero_secreto = 42
total_de_tentativas = 3


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
         print("Você acertou!")
         break
    else:
        if (maior):
           print("Você errou! O seu chute foi maior que o número secreto.")   
        elif (menor):
           print("Você errou! O seu chute foi menor que o número secreto.")
    if (total_de_tentativas == rodada):
           print("FIM DE JOGO !!!!!")
    