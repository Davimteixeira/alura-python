class Conta:
        def __init__(self, numero, titular, saldo, limite):
        # esse é o construtor com seus atributos
        # o _ mostra que esse atributo é privado
              print('construindo o objeto... {}'.format(self))
              self._numero = numero
              self._titular = titular 
              self._saldo = saldo
              self._limite = limite

        def extrato(self):
            print("o saldo de {} do titular {}".format(self._saldo, self._titular)) 
        # a função def extrato é um metodo
        def deposita(self, valor):
            self._saldo -= valor 
         # a função def deposita é um metodo
        def _pode_sacar(self, valor_a_sacar):
            valor_disponivel_a_sacar = self._saldo + self._limite
            return valor_a_sacar <= (valor_disponivel_a_sacar)
        def saca(self, valor):
            if(self._pode_sacar(valor)):
              self._saldo -= valor
         # a função def saca é um metodo
        def transfere(self, valor, destino):
            self.saca(valor) 
            destino = self.deposita(valor)
         # a função def transfere é um metodo
        @property
        def saldo(self):
            return self._saldo

        @property
        def titular(self):
            return self._titular 

        @property
        def limite(self):
            return self._limite

        @limite.setter
        def limite(self, limite):
            self._limite = limite
        @staticmethod
        def codico_banco(self):
            return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
