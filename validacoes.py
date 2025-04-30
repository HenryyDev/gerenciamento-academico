def validacao_input_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")
def validacao_nome(nome):
    if  nome.isnumeric():
        print("\nNome inválido! O nome não pode conter apenas números.")
        return False
    elif not nome:
        print("\nNome inválido! O nome não pode estar vazio.")
        return False
    return True

def validacao_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit(): ##verifica se o cpf tem 11 digitos e se é numerico
        print("\nCPF inválido! O CPF deve conter 11 dígitos numéricos e não pode ser vazio.")
        return False
    return True

def pause():
    input("Pressione ENTER para continuar")