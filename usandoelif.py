print('---------------------------------')
print('bem vindo ao jogo de adivinhação')
print('---------------------------------')

numero_secreto = 42

chute_str = input('digite seu numero: ')

print('voce digitou', chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
        
        print('FIM DE JOGO !!!!!!!')