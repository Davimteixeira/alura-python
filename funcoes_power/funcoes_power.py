# funções lambda
multiplicar = lambda x : x*2
print(multiplicar(2))

absoluto = lambda x, y : abs(x-y) < 3
print(absoluto(2,4))

operacoes = lambda x, n : x*n + x / n 
print(operacoes(10,9))

# funções map
base_numericas = [2,4,6,8,10]
aplicaveis = [1,2,3,4,5]
numeros_potenciais = list(map(pow,base_numericas, aplicaveis))
print(numeros_potenciais)

meus_numeros = [10,15,21,33,42,55]
map_numeros = list(map(lambda x : x * 2 + 8, meus_numeros))
print(map_numeros)

# funções filter
numeros = [0,4,7,2,1,0,9,3,5,6,8,0,3]
numeros = list(filter(lambda x : x != 0, numeros))
print(numeros)

nomes = ['yure alberto', 'roger guedes', 'cassio', 'fagner', 'renato algusto', 'gil', 'adriano']
print(list(filter(lambda x : x[0].lower() in 'aeiou', nomes)))

