a = int(input("escolha uma opção [1] para cadastrar novo usuário, [2] para listar usuarios cadastrados ou [3] para sair do programa: "))
usuario = []
idadeUsuario = []
while a != 3:
    if a == 1:
        n = int(input("quantos usuarios quer cadastrar?: "))
        for i in range (0, n):
            nome = str(input("digite o nome do usuario: "))
            usuario.append(nome)
            idade = int(input("digite a idade do usuario: "))
            idadeUsuario.append(idade)
        a = int(input("escolha uma opção [1] para cadastrar novo usuário, [2] para listar usuarios cadastrados ou [3] para sair do programa: "))
    elif a == 2:
        while True:
            y = len(usuario)
            for i in range(0, y):
                print (usuario[i])
                print (idadeUsuario[i])
            a = int(input("escolha uma opção [1] para cadastrar novo usuário, [2] para listar usuarios cadastrados ou [3] para sair do programa: "))
            break
    else:
        print("numero invalido")
        a = int(input("escolha uma opção [1] para cadastrar novo usuário, [2] para listar usuarios cadastrados ou [3] para sair do programa: "))
print("programa finalizado")