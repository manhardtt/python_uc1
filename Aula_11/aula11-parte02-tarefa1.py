usuarios = {}

def adicionar_usuario():
    nome = input("Nome: ")
    email = input("E-mail: ")
    usuarios[email] = {"nome": nome, "email": email}
    print("Usuário adicionado!")

def remover_usuario():
    email = input("E-mail para remover: ")
    if email in usuarios:
        del usuarios[email]
        print("Usuário removido!")
    else:
        print("E-mail não encontrado.")

def buscar_usuario():
    email = input("E-mail para buscar: ")
    usuario = usuarios.get(email)
    if usuario:
        print(f"Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    else:
        print("Usuário não encontrado.")

def listar_usuarios():
    for email, info in usuarios.items():
        print(f"{info['nome']} - {email}")

while True:
    print("\nMenu:")
    print("1. Adicionar")
    print("2. Remover")
    print("3. Buscar")
    print("4. Listar")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_usuario()
    elif opcao == "2":
        remover_usuario()
    elif opcao == "3":
        buscar_usuario()
    elif opcao == "4":
        listar_usuarios()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")