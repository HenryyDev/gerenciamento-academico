from menus import menu_principal
from estudantes import crud_estudantes
def main():
    while True:
        opcao = menu_principal()
        if opcao == 9:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            crud_estudantes()
        else:
            print("\n==========EM DESENVOLVIMENTO============\n")
main()
