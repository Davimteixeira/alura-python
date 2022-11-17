class Felino():
    nome = ""
    cor_do_pelo = ""
    juba = False
    fome_do_felino = 0

    def imprimir(self):
        print("meu pelo é:", self._nome)
        print("meu pelo é:", self.cor_do_pelo)
        if self.juba == False:
            print("eu nao tenho juba!")
        else:
            print("eu tenho juba!!!")
        if self.fome_do_felino >= 50:
            print("estou com pouca fome")
        else:
            print("estou com fome!!!!")
        
    def alimentar(self, comida):
        self.fome_do_felino += comida

    def get_nome(self):
        print("entrou no metodo getter")
        return self._nome

    def set_nome(self, novo_nome):
        print("entrou no metodo setter")
        if type(novo_nome) == type(str()):
            self._nome = novo_nome
        else:
             print("nome deve ser uma string!!")

    nome = property(get_nome, set_nome)