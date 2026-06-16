# main.py

# Dicionário (uma estrutura que guarda chave e valor, como um banco de dados simples)
credenciais = {
    "ellen": "1234"
}

def login():
    print("--- LOGIN ---")
    usuario = input("Usuario: ")
    senha = input("Senha: ")

    # Verifica se o usuario existe e se a senha está correta
    if usuario in credenciais and credenciais[usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuario ou senha incorretos.")
        return False

# Execução do programa
if login():
    print("\nBem-vindo ao Album Digital!")
    # Aqui chamaremos o menu futuramente
else:
    print("Acesso negado.")