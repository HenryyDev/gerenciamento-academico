from validacoes import validacao_input_inteiro
def menu_principal():
    opcoes = [
        ["1", "Gerenciar estudantes"],
        ["2", "Gerenciar professores"],
        ["3", "Gerenciar disciplinas"],   
        ["4", "Gerenciar turmas"],     
        ["5", "Gerenciar matriculas"],  
        ["9", "Sair"], 
    ]
    print("+-----------MENU PRINCIPAL------------+\n")
    for opcao in opcoes:
        print(f"| ({opcao[0]})  {opcao[1]:<30} |")
    print("\n+-------------------------------------+")
    return validacao_input_inteiro("Escolha a opção desejada: ")

def menu_crud(opcao_selecionada):
    print(f"\n****[{opcao_selecionada}] MENU DE OPERAÇÕES*****\n")
    opcoes = [
        ["1", "Incluir"],
        ["2", "Listar"],
        ["3", "Atualizar"],
        ["4", "Excluir"],
        ["9", "Voltar ao menu principal"],
    ]
    for opcao in opcoes:
        print(f"| ({opcao[0]})  {opcao[1]:<30} |")
    print("\n+-------------------------------------+")
    return validacao_input_inteiro("Informe a ação desejada: ")