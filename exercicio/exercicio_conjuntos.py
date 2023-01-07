def contaVogais(frase):
    vogais = {'A','E','I','O','U','a','e','i','o','u'}
    nvogais = 0
    for letra in frase:
        if letra in vogais:
            nvogais += 1
        print(f'Quantidades de vogais: {nvogais}')
        return None
# programa inicial 
lida = input('Digite a frase: ')
contaVogais(lida)