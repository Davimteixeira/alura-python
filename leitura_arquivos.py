# def criaPts(nome, qtd, min, max):
#     from random import randint
#     arq = open(nome, 'w')
#     for pos in range(qtd):
#         arq.write(str(randint(min,max))+""+str(randint(min,max))+'\n')
# Subporgramas
# def centroide(nome):
#     arquivo = open(nome,'r')
#     qtdPts = 0
#     somaX = 0
#     somaY = 0
#     for coordenada in arquivo:
#         partes = coordenada.split()
#         somaX += float(partes[0])
#         somaY += float(partes[1])
#         qtdPts+= 1
#     arquivo.close()
#     if qtdPts == 0:
#         print(arquivo.name, '-vazio!!!')
#     else:
#         print('Ponto calculado: (', somaX/qtdPts,',', somaY/qtdPts,')')
#         return None
# centroide('Pontos.txt')