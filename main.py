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
    while True:
      print("+-----------MENU PRINCIPAL------------+\n")

      for opcoes_menu_principal in opcao_menu_principal:
         print(f"| ({opcoes_menu_principal[0]:<1})  {opcoes_menu_principal[1]:<30} |")
      
      print("\n+-------------------------------------+")
      try:
         opcao_selecionada=int(input("escolha a opção desejada:"))
      except ValueError:
          print("Opção inválida. Por favor, insira um número.")
          continue

      if opcao_selecionada==9:
         print("Saindo do programa...")
         break

      if opcao_selecionada in [1, 2, 3, 4, 5]:
         
         opcoes = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]
         while True:
            print(f"\n****[{opcoes[opcao_selecionada-1]}] MENU DE OPERAÇÕES*****\n")
            
            for opcoes_crud in opcao_crud:
               print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
            print("\n+-------------------------------------+")   
            try:
               acao_desejada=int(input("Informe a ação desejada: "))
               if acao_desejada == 9:
                  break 
               if acao_desejada==1:
                  print("========== INCLUINDO ==================")
                  print("Aguarde...")
                  continue
               elif acao_desejada==2:
                  print("========== LISTANDO ===================")
                  print("Aguarde...")
                  continue
               elif acao_desejada==3:
                  print("========== ATUALIZANDO ================")
                  print("Aguarde...")
                  continue
               elif acao_desejada==4:
                  print("========== EXCLUINDO ==================")
                  print("Aguarde...")
                  continue
            except ValueError:
               print("Açao invalida tente novamente")
           
      
         
        
main()