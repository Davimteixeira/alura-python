from conta import Conta
conta = Conta('123','carla' ,100, 1000)
conta1 = Conta('12334','davi' ,134, 1500)
conta.saca(100)
conta1.deposita(100)
print(conta.extrato)
print(conta1.extrato)