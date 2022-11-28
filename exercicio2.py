class Bolacha:
        def __init__(self, descricao, valor, peso_do_pacote,):
            self._descricao = descricao
            self._valor = valor
            self._peso_do_pacote = peso_do_pacote
            self._taxa = 10
            self._taxa_de_importacao = 15 
        @property
        def descricao(self,):
            return self._descricao
        @property
        def valor(self):
            return self._valor
        
        @valor.setter
        def valor(self, valor):
            self._valor = valor
        @property
        def peso_do_pacote(self):
            return self._peso_do_pacote
        
        @property
        def taxa(self):
            return self._taxa
        @taxa.setter
        def taxa(self, taxa):
            self._taxa = taxa
        @property
        def taxa_de_importacao(self):
            return self._taxa_de_importacao
    
        @taxa_de_importacao.setter
        def taxa_de_importacao(self, taxa_de_importacao):
           self._taxa_de_importacao = taxa_de_importacao
        
        def calculo_taxa(self):
            pass

class Bolacha_comum(Bolacha):
    def __init__(self, descricao, valor, peso_do_pacote):
        super().__init__(descricao, valor, peso_do_pacote)

