from collections import namedtuple
import os
from menus import menu_crud
from validacoes import validacao_input_inteiro,pause
from armazenamento import salvar_lista, carregar_lista
dados_matriculas = namedtuple("dados_matriculas", ["codigo_turma","codigo_estudante"])
matriculas = []
PASTA_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
ARQUIVO_MATRICULAS = os.path.join(PASTA_DADOS, "matriculas.json")
matriculas = carregar_lista(ARQUIVO_MATRICULAS, dados_matriculas)
def incluir_matriculas():
    print("========== INCLUSÃO MATRICULAS ====================")
    codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
    codigo_estudante = validacao_input_inteiro("Digite o código do estudante: ")
    if any(m.codigo_turma == codigo_turma and m.codigo_estudante == codigo_estudante for m in matriculas):
        print("Já existe uma matrícula com esse código de turma e estudante.")
    else:
        matricula = dados_matriculas(codigo_turma, codigo_estudante)
        matriculas.append(matricula)
        salvar_lista(ARQUIVO_MATRICULAS, matriculas)
        print("Solicitação de inclusão concluída com sucesso!")
    pause()

def listar_matriculas():
    print("==========LISTAGEM MATRICULAS===============")
    if not matriculas:
        print("==== Não há matriculas cadastradas ====")
    else:
        print("+-------------------------------------+")
        print("| Código turma  | codigo aluno        |")
        print("+-------------------------------------+")
        for e in matriculas:
            print(f"| {e.codigo_turma:<14} | {e.codigo_estudante:<14}     |  ")
        print("+-------------------------------------+")
    pause()

def atualizar_matriculas():
    print("========== ATUALIZAR MATRICULAS ===========")
    if not matriculas:
        print("==== Não há matriculas cadastradas ====")
        return
    codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
    for i, e in enumerate(matriculas):
        if e.codigo_turma == codigo_turma:
            print(f"turma encontrada: {matriculas[i].codigo_turma}")
            codigo_estudante = validacao_input_inteiro("Digite o código do estudante: ")
            
            matriculas[i] = dados_matriculas(codigo_turma, codigo_estudante)
            salvar_lista(ARQUIVO_MATRICULAS, matriculas) 
            print("Dados atualizados com sucesso!")
            pause()
            return
    print("matricula não encontrada.")
    pause()

def excluir_matriculas():
    print("========== EXCLUSÃO MATRICULAS=============")
    if not matriculas:
        print("==== Não há matriculas cadastradas ====")
        return
    codigo_turma = validacao_input_inteiro("Digite o código da turma: ")
    for i, e in enumerate(matriculas):
        if e.codigo_turma == codigo_turma:
            confirmacao = input(f"Confirmar exclusão de {e.codigo_estudante}? (s/n): ")
            if confirmacao.lower() == 's':
                matriculas.pop(i)
                salvar_lista(ARQUIVO_MATRICULAS, matriculas)
                print("matricula excluída com sucesso.")
            else:
                print("Exclusão cancelada.")
            pause()
            return
    print("matricula não encontrada.")
    pause()

def crud_matriculas():
    while True:
        opcao = menu_crud("MATRICULAS")
        if opcao == 9:
            break
        elif opcao == 1:
            incluir_matriculas()
        elif opcao == 2:
            listar_matriculas()
        elif opcao == 3:
            atualizar_matriculas()
        elif opcao == 4:
            excluir_matriculas()
        else:
            print("Opção inválida.")



