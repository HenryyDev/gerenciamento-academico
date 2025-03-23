def main():
    opcao_menu_principal= [
            ["1", "Gerenciar estudantes"],
            ["2", "Gerenciar professores"],
            ["3", "Gerenciar disciplinas"],   
            ["4", "Gerenciar turmas"],     
            ["5", "Gerenciar matriculas"],  
            ["9", "sair"], 
        ]
    opcao_crud=[
        ["1","Incluir"],
        ["2","Listar"],
        ["3","Atualizar"],
        ["4","Excluir"],
        ["9","Voltar ao menu principal"],
    ]

    print("+-----------MENU PRINCIPAL------------+\n")

    for opcoes_menu_principal in opcao_menu_principal:
        print(f"| ({opcoes_menu_principal[0]:<1})  {opcoes_menu_principal[1]:<30} |")
    
    print("\n+-------------------------------------+")

    opcao_selecionada=int(input("escolha a opção desejada:"))

    if opcao_selecionada==1:
        print(f"\n****[ESTUDANTES] MENU DE OPERAÇÕES*****\n")

        for opcoes_crud in opcao_crud:
            print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
        print("\n+-------------------------------------+")

        acao_desejada=int(input("Informe a ação desejada: "))
        if acao_desejada==1:
           print("\n========== INCLUINDO ==================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==2:
           print("\n========== LISTANDO ===================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==3:
           print("\n========== ATUALIZANDO ================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==4:
           print("\n========== EXCLUINDO ==================")
           print("\nFinalizando aplicação...")

    elif opcao_selecionada==2:
        print(f"\n****[PROFESSORES] MENU DE OPERAÇÕES*****\n")
        
        for opcoes_crud in opcao_crud:
            print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
        print("\n+-------------------------------------+")

        acao_desejada=int(input("Informe a ação desejada: "))
        if acao_desejada==1:
           print("\n========== INCLUINDO ==================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==2:
           print("\n========== LISTANDO ===================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==3:
           print("\n========== ATUALIZANDO ================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==4:
           print("\n========== EXCLUINDO ==================")
           print("\nFinalizando aplicação...")
    
    elif opcao_selecionada==3:
        print(f"\n****[DISCIPLINAS] MENU DE OPERAÇÕES****\n")
        
        for opcoes_crud in opcao_crud:
            print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
        print("\n+-------------------------------------+")

        acao_desejada=int(input("Informe a ação desejada: "))
        if acao_desejada==1:
           print("\n========== INCLUINDO ==================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==2:
           print("\n========== LISTANDO ===================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==3:
           print("\n========== ATUALIZANDO ================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==4:
           print("\n========== EXCLUINDO ==================")
           print("\nFinalizando aplicação...")
    elif opcao_selecionada==4:
        print(f"\n******[TURMAS] MENU DE OPERAÇÕES*******\n")
        
        for opcoes_crud in opcao_crud:
            print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
        print("\n+-------------------------------------+")

        acao_desejada=int(input("Informe a ação desejada: "))
        if acao_desejada==1:
           print("\n========== INCLUINDO ==================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==2:
           print("\n========== LISTANDO ===================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==3:
           print("\n========== ATUALIZANDO ================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==4:
           print("\n========== EXCLUINDO ==================")
           print("\nFinalizando aplicação...")

    elif opcao_selecionada==5:
        print(f"\n****[MATRÍCULAS] MENU DE OPERAÇÕES****\n")
        
        for opcoes_crud in opcao_crud:
            print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
        print("\n+-------------------------------------+")

        acao_desejada=int(input("Informe a ação desejada: "))
        if acao_desejada==1:
           print("\n========== INCLUINDO ==================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==2:
           print("\n========== LISTANDO ===================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==3:
           print("\n========== ATUALIZANDO ================")
           print("\nFinalizando aplicação...")
        elif acao_desejada==4:
           print("\n========== EXCLUINDO ==================")
           print("\nFinalizando aplicação...")
        
        
main()