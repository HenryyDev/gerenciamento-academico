from collections import namedtuple
from menus import menu_crud
from validacoes import validacao_nome, validacao_cpf, validacao_input_inteiro

dados_professores = namedtuple("dados_professores", ["codigo", "nome", "cpf"])
professores = []

def incluir_professores():
    print("========== INCLUSÃO PROFESSORES ====================")
    # Código do professor
    codigo = validacao_input_inteiro("Digite o código do professor: ")
    # Nome do professor
    while True:
        nome = input("Digite o nome do professor: ").strip()
        if validacao_nome(nome):
            break

    # CPF do professor
    while True:
        cpf = input("Digite o CPF do professor: ").strip()
        if validacao_cpf(cpf):
            break

    # Se tudo estiver válido, cria e adiciona o professor
    professor = dados_professores(codigo, nome, cpf)
    professores.append(professor)
    print("Solicitação de inclusão concluída com sucesso!")
    pause()

def listar_professores():
    print("==========LISTAGEM PROFESSORES===============")
    if not professores:
        print("==== Não há professores cadastrados ====")
    else:
        print("+-------------------------------------+")
        print("| Código   | Nome           | CPF           ")
        print("+-------------------------------------+")
        for e in professores:
            print(f"| {e.codigo:<8} | {e.nome:<14} | {e.cpf:<12} ")
        print("+-------------------------------------+")
    pause()

def atualizar_professor():
    print("========== ATUALIZAR PROFESSORES ===========")
    if not professores:
        print("==== Não há professores cadastrados ====")
        return
    codigo = validacao_input_inteiro("Digite o código do professor: ")
    for i, e in enumerate(professores):
        if e.codigo == codigo:
            print(f"professor encontrado: {professores[i].nome}")
            while True:
                nome = input("Digite o novo nome: ").strip()
                if validacao_nome(nome):        
                    break
            while True: 
                cpf = input("Digite o novo CPF: ").strip()
                if validacao_cpf(cpf):
                    break
            professores[i] = dados_professores(codigo, nome, cpf) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("professor não encontrado.")
    pause()

def excluir_professor():
    print("========== EXCLUSÃO PROFESSORES=============")
    if not professores:
        print("==== Não há professores cadastrados ====")
        return
    codigo = validacao_input_inteiro("Digite o código do professor: ")
    for i, e in enumerate(professores):
        if e.codigo == codigo:
            confirmacao = input(f"Confirmar exclusão de {e.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                professores.pop(i)
                print("professor excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("professor não encontrado.")
    pause()

def crud_professores():
    while True:
        opcao = menu_crud("PROFESSORES")
        if opcao == 9:
            break
        elif opcao == 1:
            incluir_professores()
        elif opcao == 2:
            listar_professores()
        elif opcao == 3:
            atualizar_professor()
        elif opcao == 4:
            excluir_professor()
        else:
            print("Opção inválida.")

def pause():
    input("Pressione ENTER para continuar")

