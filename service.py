import storage

def adicionar_usuario(nome, email):
    usuarios = storage.carregar_dados()
    usuarios.append({"nome": nome, "email": email})
    storage.salvar_dados(usuarios)
    return True

def listar_usuarios():
    return storage.carregar_dados()

def buscar_usuario(email):
    for u in storage.carregar_dados():
        if u["email"] == email:
            return u
    return None
