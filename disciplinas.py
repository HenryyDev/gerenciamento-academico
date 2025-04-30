from collections import namedtuple
from menus import menu_crud
from validacoes import validacao_nome, validacao_input_inteiro

dados_disciplinas = namedtuple("dados_disciplinas", ["codigo", "nome"])
disciplinas = []

def incluir_disciplinas():
    print("========== INCLUSÃO DISCIPLINAS ====================")
    # Código da disciplina
    codigo = validacao_input_inteiro("Digite o código da disciplina: ")
    # Nome da disciplina
    while True:
        nome = input("Digite o nome da disciplina: ").strip()
        if validacao_nome(nome):
            break
    disciplina = dados_disciplinas(codigo, nome)
    disciplinas.append(disciplina)
    print("Solicitação de inclusão concluída com sucesso!")
    pause()

def listar_disciplinas():
    print("==========LISTAGEM DISCIPLINAS===============")
    if not disciplinas:
        print("==== Não há disciplinas cadastradas ====")
    else:
        print("+-------------------------------------+")
        print("| Código   | Nome                    |")
        print("+-------------------------------------+")
        for e in disciplinas:
            print(f"| {e.codigo:<8} | {e.nome:<14} | ")
        print("+-------------------------------------+")
    pause()

def atualizar_disciplinas():
    print("========== ATUALIZAR DISCIPLINAS ===========")
    if not disciplinas:
        print("==== Não há disciplinas cadastradas ====")
        return
    codigo = validacao_input_inteiro("Digite o código da disciplina: ")
    for i, e in enumerate(disciplinas):
        if e.codigo == codigo:
            print(f"disciplina encontrada: {disciplinas[i].nome}")
            while True:
                nome = input("Digite o novo nome: ").strip()
                if validacao_nome(nome):        
                    break
            disciplinas[i] = dados_disciplinas(codigo, nome) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("disciplinas não encontrado.")
    pause()

def excluir_disciplinas():
    print("========== EXCLUSÃO DISCIPLINAS=============")
    if not disciplinas:
        print("==== Não há disciplinas cadastradas ====")
        return
    codigo = validacao_input_inteiro("Digite o código da disciplina: ")
    for i, e in enumerate(disciplinas):
        if e.codigo == codigo:
            confirmacao = input(f"Confirmar exclusão de {e.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                disciplinas.pop(i)
                print("disciplinas excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("disciplinas não encontrado.")
    pause()

def crud_disciplinas():
    while True:
        opcao = menu_crud("DISCIPLINAS")
        if opcao == 9:
            break
        elif opcao == 1:
            incluir_disciplinas()
        elif opcao == 2:
            listar_disciplinas()
        elif opcao == 3:
            atualizar_disciplinas()
        elif opcao == 4:
            excluir_disciplinas()
        else:
            print("Opção inválida.")

def pause():
    input("Pressione ENTER para continuar")

