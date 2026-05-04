try:
    import storage
except ImportError:
    pass

def adicionar_usuario(nome, email):
    """
    Recebe os dados, aplica regras e manda salvar.
    """
    # 1. Tenta carregar a lista atual do banco de dados
    try:
        usuarios = storage.carregar_dados()
    except NameError:
        print("Aviso: Módulo storage ainda não integrado. Simulando dados vazios.")
        usuarios = []

    # 2. Cria o formato do usuário
    novo_usuario = {
        "nome": nome,
        "email": email
    }

    # 3. Adiciona na lista e salva
    usuarios.append(novo_usuario)
    
    try:
        storage.salvar_dados(usuarios)
        return True
    except NameError:
        print("Aviso: Módulo storage ainda não integrado. Usuário não foi salvo de verdade.")
        return False

def listar_usuarios():
    """
    Retorna a lista de todos os usuários cadastrados.
    """
    try:
        return storage.carregar_dados()
    except NameError:
        print("Aviso: Módulo storage ainda não integrado.")
        return []