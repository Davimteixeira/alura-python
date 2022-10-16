print('SISTEMA DE AUTORIZAÇÃO')
usuario = input("Informe o usuário do sistema:\n")
autorizados = ["Flávio", "Douglas", "Nico", "flavio", "douglas", "nico"]

if usuario in autorizados:
    print(f"Seja bem-vindo {usuario}!")
else:
    print(f"Seu usario {usuario} não condiz com os usarios cadrastados !!!")

