class Racao :
    def _init_(self,raca,tamanho,peso,quilo) :
        self.raca = raca
        self.tamanho = tamanho
        self.peso = peso
        self.quilo = quilo
        self.preco = 0
    def pedir_marca (self) :
        while True :
            sua_marca = str(input('Digite [1]Premier[2]Petlove[3]Pedigree: '))
            if sua_marca != '1' and sua_marca != '2' and sua_marca != '3' :
                print('Nao temos uma racao assim')
                continue
            else :
                lista_racao=[0,'Premier','Petlove','Pedigree']
                self.marca = lista_racao [int(sua_marca)]
                break
    def mostrar_marca (self) :
        print (f'marca escolhida {self.marca}')
    def pedir_tipo (self) :   
        while True :
            seu_tipo = str(input('Digite [1]Solida[2]Pastosa : '))
            if seu_tipo != '1'  and seu_tipo != '2' :
                print('nao temos esse tipo de escolha na loja')
                continue
            else :
                tipos = [0,'Solida','Pastosa']
            self.tipo = tipos[int(seu_tipo)]
            break
    def mostrar_tipo(self) :
        print (f'seu tipo de raçao foi {self.tipo}')
        if self.tipo == 'Pastosa' :
            print('como escolheu pastosa o preço total aumentar em 15R$')
        if self.tipo == 'Solida' :
            print('como escolheu solida o preço total aumentar em 10R$')
    def pagar (self,dinhero) :
        if type(dinhero) == type(float()) : 
            if dinhero <=0 :
                print('dinhero insuficiente')
            elif dinhero < self.preco :
                print(f'dinnhero insuficiente para realizar a conta falta {self.preco - dinhero}')
            else :
                print('compra bem sucedida volte sempre')
        else :
            print('dinhero invalido')
    def calcular_conta (self) :
        if self.tipo == 'Pastosa' :
            self.preco = 15 + (self.preco * self.quilo )
            print(f'seu preço foi {self.preco}')
        elif self.tipo ==  'Solida' :
            self.preco = 10 + (self.preco * self.quilo )
            print(f'seu preço foi {self.preco}')
    #def get_all(self):
        #   [
        #      self.pedir_marca(),
        #    self.pedir_sabor(),
        #    self.mostrar_sabor() ,
        #    self.pedir_tipo(),
        #    self.mostrar_tipo(),
        #    self.preco_alimento(),
        #    self.calcular_conta(),
        #    self.pagar(60.0),
        #]
class Equino (Racao) :
    def _init_(self, raca, tamanho, peso,quilo):
        super()._init_(raca, tamanho, peso,quilo)
    def pedir_sabor (self) :
        print('Ração para equinos 10 R$')
        seu_sabor = str(input('Digite [1]Milho[2]Cenoura[3]Alfalfa: '))
        while True :
            if seu_sabor != '1' and seu_sabor != '2' and seu_sabor != '3' :
                print('sabor indisponivel na loja')
                continue
            else :
                sabores = [0,'Milho','Cenoura','Alfalfa']
                self.sabor = sabores[int(seu_sabor)]
                break
    def mostrar_sabor (self) :
        print(f'seu sabor escolhido foi {self.sabor}')
    def preco_alimento (self) :
        self.preco = 10
class Caprinos (Racao) :
    def _init_(self, raca, tamanho, peso,quilo):
        super()._init_(raca, tamanho, peso,quilo)
        self.quilo = quilo
    def pedir_sabor (self) :
        print('Ração para caprinos 5 R$ o quilo')
        while True :
            seu_sabor = str(input('Digite [1]Milho[2]Caju[3]Resido: '))
            if seu_sabor != '1' and seu_sabor != '2' and seu_sabor != '3' :
                print('sabor indisponivel na loja')
                continue
            else :
                sabores = [0,'Milho','Caju','Resido']
                self.sabor = sabores[int(seu_sabor)]
                break
    def mostrar_sabor (self) :
        print(f'seu sabor escolhido foi {self.sabor}')
    def preco_alimento (self) :
        self.preco = 5