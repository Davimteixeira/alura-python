#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe BombaCombustivel abaixo sabemos que é uma bomba de gasolina e:
# atributos: valor_do_litro e quantidade_de_combustivel
# todos atributos encapsulados fortemente
# métodos abaixo:
# abastecer_a_bomba - esse método abastece a bomba para iniciar a venda
# abastecer_veiculo_valor – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_veiculo_litro – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente
# alterar_valor – altera o valor do litro do combustível
# alterar_quantidade_combustivel – altera a quantidade combustível restante na bomba
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
# OBS: Faça a impressão dos elementos

class BombaCombustivel:
    def __init__(self, valor_do_litro):
        self.__valor_do_litro = valor_do_litro
        self.__quantidade_de_combustivel = 0 
        
    @property
    def valor_do_litro(self):
        return self.valor_do_litro
    
    valor_do_litro.setter
    def valor_do_litro(self, novo_valor):
        if type(novo_valor) == type(float()):
            self.valor_do_litro = novo_valor
        else:
            print('digite valor real')

    def abastecer(self, litros):
        abastecer = float(input('Quanto você quer abastecer? '))
        
        
        
        
        
        
        # while type(litros) == type(str()):
        #     self.__quantidade_de_combustivel = litros
        #     if litros <= 40 :
        #         self.__quantidade_de_combustivel = litros
        #     else:
        #         print('a bomba não recebe mais que 40 litros')
        #     if litros <= 1 :
        #         print('voce não pode colocar numeros negativos')
            
                
ze = BombaCombustivel(11)
ze.abastecer