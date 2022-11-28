class Aluno():
        def __init__ (self, indentificador, nome, idade, peso, altura):
            print('construindo o objeto')
            self.__indentificador = indentificador
            self.__nome = nome 
            self.__idade = idade 
            self.__peso = peso
            self.__altura = altura 
        
        @property
        def indentificador(self):
            return self.__indentificador
            
        @property
        def nome(self):
            return self.__nome
        
        @property
        def idade(self):
            return self.__idade
        
        @idade.setter
        def idade(self, idade):
            self.__idade = idade
        
        @property 
        def peso(self):
            return self.__peso
        
        @peso.setter
        def peso(self, peso):
            self.__peso = peso
        
        @property
        def altura(self):
            return self.__altura   
        
        @altura.setter
        def altura(self, altura):
            self.__altura = altura
            
        
        def calculo_imc(self):
            self.__peso // (self.__altura ** 2)
        
        def __str__(self):
            return f"  {self.__indentificador}, {self.__nome}, {self.__idade}, {self.__peso}"
        
    