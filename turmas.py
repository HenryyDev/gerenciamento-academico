from collections import namedtuple
from menus import menu_crud
from validacoes import validacao_input_inteiro,pause
from armazenamento import salvar_lista, carregar_lista
dados_turmas = namedtuple("dados_turmas", ["codigo_turma", "codigo_professor","codigo_disciplina"])
turmas = []
ARQUIVO_TURMAS = "turmas.json"
turmas = carregar_lista(ARQUIVO_TURMAS, dados_turmas)

def incluir_turmas():
    print("========== INCLUSÃO TURMAS ====================")
   
    while True:
        codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
        if any(t.codigo == codigo_turma for t in turmas):
            print("Já existe uma turma com esse código. Tente outro.")
        else:
            break
    codigo_professor = validacao_input_inteiro("Digite o código do professor: ")
    codigo_disciplina= validacao_input_inteiro("Digite o código da disciplina: ") 
    disciplina = dados_turmas(codigo_turma,codigo_professor,codigo_disciplina)
    turmas.append(disciplina)
    salvar_lista(ARQUIVO_TURMAS, turmas)
    print("Solicitação de inclusão concluída com sucesso!")
    pause()

def listar_turmas():
    print("==========LISTAGEM TURMAS===============")
    if not turmas:
        print("==== Não há turmas cadastradas ====")
    else:
        print("+-------------------------------------+")
        print("| Código turma  | codigo professor |codigo disciplina|")
        print("+-------------------------------------+")
        for e in turmas:
            print(f"| {e.codigo_turma:<14} | {e.codigo_professor:<14} | {e.codigo_disciplina:<14}  ")
        print("+-------------------------------------+")
    pause()

def atualizar_turmas():
    print("========== ATUALIZAR TURMAS ===========")
    if not turmas:
        print("==== Não há turmas cadastradas ====")
        return
    codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
    for i, e in enumerate(turmas):
        if e.codigo_turma == codigo_turma:
            print(f"turma encontrada: {turmas[i].codigo_turma}")
            codigo_professor = validacao_input_inteiro("Digite o novo codigo do professor: ")
            codigo_disciplina= validacao_input_inteiro("Digite o novo codigo da disciplina: ")
            turmas[i] = dados_turmas(codigo_turma, codigo_professor,codigo_disciplina)
            salvar_lista(ARQUIVO_TURMAS, turmas) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("turma não encontrada.")
    pause()

def excluir_turmas():
    print("========== EXCLUSÃO TURMAS=============")
    if not turmas:
        print("==== Não há turmas cadastradas ====")
        return
    codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
    for i, e in enumerate(turmas):
        if e.codigo_turma == codigo_turma:
            confirmacao = input(f"Confirmar exclusão de {e.codigo_professor}? (s/n): ")
            if confirmacao.lower() == 's':
                turmas.pop(i)
                salvar_lista(ARQUIVO_TURMAS, turmas)
                print("turma excluída com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("turma não encontrada.")
    pause()

def crud_turmas():
    while True:
        opcao = menu_crud("TURMAS")
        if opcao == 9:
            break
        elif opcao == 1:
            incluir_turmas()
        elif opcao == 2:
            listar_turmas()
        elif opcao == 3:
            atualizar_turmas()
        elif opcao == 4:
            excluir_turmas()
        else:
            print("Opção inválida.")



