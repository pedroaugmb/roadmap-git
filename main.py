# main.py

# Importa as funções do service (você ou seu colega vão implementar)
from service import (
    criar_usuario,
    listar_usuarios,
    remover_usuario
)


def mostrar_menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Remover usuário")
    print("0 - Sair")


def opcao_cadastrar():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")

    try:
        criar_usuario(nome, email)
        print("✅ Usuário cadastrado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao cadastrar: {e}")


def opcao_listar():
    print("\n--- Lista de Usuários ---")

    usuarios = listar_usuarios()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nome']} - {usuario['email']}")

def opcao_remover():
    print("\n--- Remover Usuário ---")

    email = input("Digite o email do usuário a remover: ")

    try:
        remover_usuario(email)
        print("🗑️ Usuário removido com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao remover: {e}")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_cadastrar()

        elif opcao == "2":
            opcao_listar()

        elif opcao == "3":
            opcao_remover()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()