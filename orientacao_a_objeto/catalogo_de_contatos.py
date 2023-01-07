#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos conforme abaixo:
# fazer com que os contatos sejam armazenados
# validar o CPF para Pessoa Física
# validar CNPJ para pessoa Jurídica
# montar a agenda dos contatos em formato de lista.
# utilizar os métodos mágicos.
# implemente as nomenclaturas dos atributos e métodos.
# OBS: Utilize expressões regulares
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos

import re
class CatalogoContatos:
    def __init__(self,nome,idade,telefone):
        self.nome=nome
        self.idade=idade
        self.telefone=telefone
    def valida_idade(self):
        if self.idade <0 or self.idade>=130:
            raise ValueError('idade invalida')
        else:
            return self.idade
    def valida_telefone(self):
        padrao=re.compile('[0-9]{2}[ ]?[9]?[0-9]{4}-?[0-9]{4}')
        match=padrao.match(self.telefone)
        if match :
            return self.telefone
        else:
            raise ValueError('telefone invalido')
    def __str__(self):
        return(f'nome: {self.nome} idade: {self.idade} e telefone: {self.telefone}')
class CatalogoPessoaFisica(CatalogoContatos):
    def __init__(self, nome, idade, telefone,cpf):
        super().__init__(nome, idade, telefone)
        self.cpf=cpf
    def valida_cpf(self):
        self.cpf = str(self.cpf)
        padrao = re.compile("([0-9]{3}.?){2}[0-9]{3}-?[0-9]{2}")    
        busca = padrao.match(self.cpf)
        if busca :
            return self.cpf
        else:
            raise ValueError('cpf errado')
    def __str__(self):
        return(f'nome: {self.nome} telefone:{self.telefone} idade: {self.idade} e cpf: {self.cpf}')
class CatalogoPessoaJuridica(CatalogoContatos):
    def __init__(self, nome,idade, telefone,cnpj):
        super().__init__(nome, idade, telefone)
        self.cnpj=cnpj
    def valida_cnpj(self):
        padrao=re.compile("[0-9]{2}.?[0-9]{3}.?[0-9]{3}/?0001-?[0-9]{2}")
        match=padrao.match(self.cnpj)
        if match:
            return self.cnpj
        else:
            raise ValueError('cnpj errada')
    def __str__(self):
        return(f'nome: {self.nome}  telefone:{self.telefone} idade: {self.idade} e cnpj: {self.cnpj}')
class Agenda():
    def __init__(self,contato):
        self.contato=contato
    def __getitem__(self,item):
        return  self.contato[item]
    def __len__(self):
        return len(contatos)
    def __contains__(self,valor):
        return valor in self.contato
    def append(self,valor):
        self.contato.append(valor)
    @property
    def listagem(self):
        return self.contato
felipe=CatalogoContatos('felipe',10,'88 99662-8418')
felipe.valida_idade()
felipe.valida_telefone()
maria=CatalogoPessoaFisica('maria',15,'88 90992-8213','121.252.363-84')
maria.valida_telefone()
maria.valida_cpf()
maria.valida_idade()
joao=CatalogoPessoaJuridica('joao',10,'88 99662-8418','11.111.111/0001-99')
joao.valida_telefone()
joao.valida_cnpj()
joao.valida_idade()
contatos=[felipe,joao,maria]
contatos_total=Agenda(contatos)
print(f'tamanho do contatos : {contatos_total.__len__()}')
for conta in contatos_total.listagem:
    print(conta)