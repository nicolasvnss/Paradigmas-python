while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha == nome_usuario:
        print("ERRO: A senha não pode ser igual ao nome de usuário.")
    else:
        break

print("Usuário cadastrado com sucesso!")
