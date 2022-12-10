class Livro:
    def __init__(self, nome, qtdpaginas, autor, preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.__preco = preco
    
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, novo_preco):
        if type(novo_preco) == type(float()):
            self.__preco = novo_preco
        else:
          print('digite novamente')
        
livro = Livro("turma do zézé", 11, "zézé", 20)
livro.preco = 11.0
print(livro.preco)
livro.preco = 11.3
print(livro.preco)
