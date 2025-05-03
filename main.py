from menus import menu_principal
from estudantes import crud_estudantes
from professores import crud_professores
from disciplinas import crud_disciplinas
from turmas import crud_turmas
from matriculas import crud_matriculas
def main():
    while True:
        opcao = menu_principal()
        if opcao == 9:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            crud_estudantes()
        elif opcao == 2:
            crud_professores()
        elif opcao == 3:  
            crud_disciplinas()
        elif opcao == 4:
            crud_turmas()
        elif opcao == 5:
            crud_matriculas()
        else:
            print("\n==========EM DESENVOLVIMENTO============\n")
main()
