from collections import namedtuple
from menus import menu_crud
from validacoes import validacao_nome, validacao_input_inteiro,pause
from armazenamento import salvar_lista, carregar_lista
dados_disciplinas = namedtuple("dados_disciplinas", ["codigo", "nome"])
disciplinas = []
ARQUIVO_DISCIPLINAS = "disciplinas.json"
disciplinas = carregar_lista(ARQUIVO_DISCIPLINAS, dados_disciplinas)

def incluir_disciplinas():
    print("========== INCLUSÃO DISCIPLINAS ====================")
    while True:
        codigo = validacao_input_inteiro("Digite o código da disciplina: ")
        if any(d.codigo == codigo for d in disciplinas):
            print("Já existe uma disciplina com esse código. Tente outro.")
        else:
            break
    while True:
        nome = input("Digite o nome da disciplina: ").strip()
        if validacao_nome(nome):
            break
    disciplina = dados_disciplinas(codigo, nome)
    disciplinas.append(disciplina)
    salvar_lista(ARQUIVO_DISCIPLINAS, disciplinas)
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
        for d in disciplinas:
            print(f"| {d.codigo:<8} | {d.nome:<14} | ")
        print("+-------------------------------------+")
    pause()

def atualizar_disciplinas():
    print("========== ATUALIZAR DISCIPLINAS ===========")
    if not disciplinas:
        print("==== Não há disciplinas cadastradas ====")
        return
    codigo = validacao_input_inteiro("Digite o código da disciplina: ")
    for i, d in enumerate(disciplinas):
        if d.codigo == codigo:
            print(f"disciplina encontrada: {disciplinas[i].nome}")
            while True:
                nome = input("Digite o novo nome: ").strip()
                if validacao_nome(nome):        
                    break
            disciplinas[i] = dados_disciplinas(codigo, nome)
            salvar_lista(ARQUIVO_DISCIPLINAS, disciplinas) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("disciplina não encontrada.")
    pause()

def excluir_disciplinas():
    print("========== EXCLUSÃO DISCIPLINAS=============")
    if not disciplinas:
        print("==== Não há disciplinas cadastradas ====")
        return
    codigo = validacao_input_inteiro("Digite o código da disciplina: ")
    for i, d in enumerate(disciplinas):
        if d.codigo == codigo:
            confirmacao = input(f"Confirmar exclusão de {d.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                disciplinas.pop(i)
                salvar_lista(ARQUIVO_DISCIPLINAS, disciplinas)
                print("disciplina excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("disciplina não encontrada.")
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


