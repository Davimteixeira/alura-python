from datetime import datetime
class Aluno:
    def __init__(self,nome, curso,):
        self._nome = nome
        self._curso = curso
        tempo_sem_dormir = 0
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,novo_nome):
        if type(novo_nome) == type(str):
            self._nome = novo_nome
        else:
            print('voce não fez certo parceiro')
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, novo_curso):
        if type(novo_curso) == type(str):
            self._curso = novo_curso
        else:
            print('voce não fez certo parceiro')
