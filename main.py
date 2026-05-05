from service import adicionar_usuario, listar_usuarios, buscar_usuario

def criar_usuario(nome, email):
    adicionar_usuario(nome, email)
    return {"nome": nome, "email": email}

def exibir_menu():
    print("\n" + "=" * 35)
    print("     SISTEMA DE USUÁRIOS")
    print("=" * 35)
    print("  1. Criar usuário")
    print("  2. Listar usuários")
    print("  3. Buscar usuário por e-mail")
    print("  0. Sair")
    print("=" * 35)


def tela_criar_usuario():
    print("\n--- Criar Usuário ---")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    if not nome or not email:
        print("❌ Nome e e-mail são obrigatórios.")
        return

    try:
        usuario = criar_usuario(nome, email)
        print(f"✅ Usuário criado com sucesso: {usuario['nome']} ({usuario['email']})")
    except Exception as e:
        print(f"❌ Erro ao criar usuário: {e}")


def tela_listar_usuarios():
    print("\n--- Lista de Usuários ---")
    try:
        usuarios = listar_usuarios()
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for i, u in enumerate(usuarios, start=1):
            print(f"  {i}. {u['nome']} — {u['email']}")
    except Exception as e:
        print(f"❌ Erro ao listar usuários: {e}")


def tela_buscar_usuario():
    print("\n--- Buscar Usuário ---")
    email = input("Digite o e-mail: ").strip()

    if not email:
        print("❌ E-mail não pode ser vazio.")
        return

    try:
        usuario = buscar_usuario(email)
        if usuario:
            print(f"✅ Encontrado: {usuario['nome']} ({usuario['email']})")
        else:
            print("❌ Usuário não encontrado.")
    except Exception as e:
        print(f"❌ Erro na busca: {e}")


def main():
    print("Bem-vindo ao sistema!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tela_criar_usuario()
        elif opcao == "2":
            tela_listar_usuarios()
        elif opcao == "3":
            tela_buscar_usuario()
        elif opcao == "0":
            print("Saindo... Até mais! 👋")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()