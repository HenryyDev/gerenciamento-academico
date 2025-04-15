from collections import namedtuple
from menus import menu_crud
from validacoes import validacao_nome, validacao_cpf, validacao_input_inteiro

dados_estudantes = namedtuple("dados_estudantes", ["codigo", "nome", "cpf"])
estudantes = []

def incluir_estudante():
    print("========== INCLUSÃO ====================")
    # Código do estudante
    codigo = validacao_input_inteiro("Digite o código do estudante: ")
    # Nome do estudante
    while True:
        nome = input("Digite o nome do estudante: ").strip()
        if validacao_nome(nome):
            break

    # CPF do estudante
    while True:
        cpf = input("Digite o CPF do estudante: ").strip()
        if validacao_cpf(cpf):
            break

    # Se tudo estiver válido, cria e adiciona o estudante
    estudante = dados_estudantes(codigo, nome, cpf)
    estudantes.append(estudante)
    print("Solicitação de inclusão concluída com sucesso!")
    pause()

def listar_estudantes():
    print("========== LISTAGEM ====================")
    if not estudantes:
        print("==== Não há estudantes cadastrados ====")
    else:
        print("+-------------------------------------+")
        print("| Código   | Nome           | CPF           ")
        print("+-------------------------------------+")
        for e in estudantes:
            print(f"| {e.codigo:<8} | {e.nome:<14} | {e.cpf:<12} ")
        print("+-------------------------------------+")
    pause()

def atualizar_estudante():
    print("========== ATUALIZAR ==================")
    if not estudantes:
        print("==== Não há estudantes cadastrados ====")
        return
    codigo = validacao_input_inteiro("Digite o código do estudante: ")
    for i, e in enumerate(estudantes):
        if e.codigo == codigo:
            print(f"Estudante encontrado: {estudantes[i].nome}")
            while True:
                nome = input("Digite o novo nome: ").strip()
                if validacao_nome(nome):        
                    break
            while True: 
                cpf = input("Digite o novo CPF: ").strip()
                if validacao_cpf(cpf):
                    break
            estudantes[i] = dados_estudantes(codigo, nome, cpf) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("Estudante não encontrado.")
    pause()

def excluir_estudante():
    print("========== EXCLUSÃO ===================")
    if not estudantes:
        print("==== Não há estudantes cadastrados ====")
        return
    codigo = validacao_input_inteiro("Digite o código do estudante: ")
    for i, e in enumerate(estudantes):
        if e.codigo == codigo:
            confirmacao = input(f"Confirmar exclusão de {e.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                estudantes.pop(i)
                print("Estudante excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("Estudante não encontrado.")
    pause()

def crud_estudantes():
    while True:
        opcao = menu_crud("ESTUDANTES")
        if opcao == 9:
            break
        elif opcao == 1:
            incluir_estudante()
        elif opcao == 2:
            listar_estudantes()
        elif opcao == 3:
            atualizar_estudante()
        elif opcao == 4:
            excluir_estudante()
        else:
            print("Opção inválida.")

def pause():
    input("Pressione ENTER para continuar")

