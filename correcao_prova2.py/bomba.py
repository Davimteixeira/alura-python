
class BombaCombustivel:
    def __init__(self, valor_do_litro):
        self.__valor_do_litro = valor_do_litro
        self.__quantidade_de_combustivel = 0.0

    @property
    def valor_do_litro(self):
        return self.__valor_do_litro

    @property
    def quantidade_de_combustivel(self):
        return self.__quantidade_de_combustivel

    @valor_do_litro.setter
    def valor_do_litro(self, novo_valor):
        if type(novo_valor) == type(float()):
            self.__valor_do_litro = novo_valor
        else:
            print("Preço deve ser do tipo float!")
    
    @quantidade_de_combustivel.setter
    def quantidade_de_combustivel(self, nova_quantidade):
        if type(nova_quantidade) == type(float()):
            self.__quantidade_de_combustivel = nova_quantidade
        else:
            print("Quantidade de combustivel deve ser um numro inteiro!")
    
    def abastecer_bomba(self, quantidade_litros):
        calcula_quantidade = self.__quantidade_de_combustivel + quantidade_litros
        if  calcula_quantidade < 1000.00:
            print(f'Foi abastecido {quantidade_litros:.2f}L na bomba')
            self.quantidade_de_combustivel += quantidade_litros
        else:
            print(f'Impossivel abastecer {quantidade_litros:.2f} litros')

    def abastecer_veiculo(self, valor = 0.00, litros = 0.00):
        if self.quantidade_de_combustivel != 0.00:
            if valor != 0.00:
                abastecer_veiculo_valor = valor/self.valor_do_litro
                self.quantidade_de_combustivel -= abastecer_veiculo_valor
                print(f'Você pagou R${valor:.2f} e seu abastecimento é de {abastecer_veiculo_valor:.2f}L. A bomba atualizada tem {self.quantidade_de_combustivel:.2f}L')
            elif litros != 0:
                abastecer_veiculo_litro = litros * self.valor_do_litro
                self.quantidade_de_combustivel -= litros
                print(f'Você solicitou {litros:.2f}L e vai pagar R${abastecer_veiculo_litro:.2f} pelo seu abastecimento. A bomba atualizada tem {self.quantidade_de_combustivel:.2f}L')
            else:
                print("Verifique as informações, não conseguimos processar sua solicitação.")
        else:
            print(f'Impossivel abastercer. A bomba está com {self.quantidade_de_combustivel:.2f} litros, favor abastercer a bomba.')
    
    def __str__(self):
        return f'Na bomba tem {self.quantidade_de_combustivel:.2f} litros e o valor do litro de gasolina é R${self.valor_do_litro:.2f}.'

posto01 = BombaCombustivel('ww')
print(posto01.valor_do_litro)
print("*"*20)
print(posto01)
posto01.abastecer_veiculo(valor = 50.00)
print("*"*20)
posto01.abastecer_bomba(300.0)
print("*"*20)
print(posto01)
print("*"*20)
posto01.abastecer_veiculo(valor = 20.00)
print("*"*20)
posto01.abastecer_bomba(400.0)
print("*"*20)
print(posto01)
posto01.abastecer_bomba(300.0)
print("*"*20)
posto01.abastecer_veiculo(valor = 32.00)
print("*"*20)
print(posto01)
posto01.abastecer_bomba(300.0)
print("*"*20)
print(posto01)
print("*"*20)
posto01.abastecer_veiculo(litros = 10.00)
print("*"*20)
print(posto01)