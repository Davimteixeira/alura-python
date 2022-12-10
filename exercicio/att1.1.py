class Livro():
    def __init__(self, nome, qtdPaginas, autor):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
      


    def get_preco(self):
        return self.__preco
    
    def set_preco(self,novo_preco):
        if type(novo_preco) == type(float()):
            self.__preco = novo_preco
        else:
            print("Preço deve ser do tipo float")

    
    
    def __str__(self):
            return f"O {self.__class__.__name__} {Gibi.nome} do autor {self.autor} tem {self.qtdPaginas} páginas e custa R$ {self.get_preco()}"
    
    preco = property(get_preco, set_preco)





Gibi = Livro("Turma da Mônica", 22, "Mauricio de Sousa")
print("="*20)
Gibi.set_preco(7.50) 
print(Gibi.get_preco())   
print("="*20)
print(Gibi)