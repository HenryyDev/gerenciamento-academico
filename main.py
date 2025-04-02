# Nome: Henrique Luiz Ribeiro 
# Curso: Análise e desenvolvimento de sistemas

# função principal 
def main():
   # matriz contendo as op do menu principal
    opcao_menu_principal= [
            ["1", "Gerenciar estudantes"],
            ["2", "Gerenciar professores"],
            ["3", "Gerenciar disciplinas"],   
            ["4", "Gerenciar turmas"],     
            ["5", "Gerenciar matriculas"],  
            ["9", "sair"], 
        ]
    # matriz contendo as op de crud
    opcao_crud=[
        ["1","Incluir"],
        ["2","Listar"],
        ["3","Atualizar"],
        ["4","Excluir"],
        ["9","Voltar ao menu principal"],
    ]

    #array para armazenar estudantes
    estudantes=[]

    # loop principal do sistema
    while True:
      print("+-----------MENU PRINCIPAL------------+\n")
      #loop para o menu principal que itera a matriz com as op e armazena cada elemento na variavel opcoes_menu_principal
      for opcoes_menu_principal in opcao_menu_principal:
         print(f"| ({opcoes_menu_principal[0]:<1})  {opcoes_menu_principal[1]:<30} |")
      
      print("\n+-------------------------------------+")
      # validação para erro de valor
      try:
         opcao_selecionada=int(input("escolha a opção desejada:"))
      except ValueError:
          print("Opção inválida! Tente novamente.")
          continue
      #if para o fechamento do programa
      if opcao_selecionada==9:
         print("Saindo do programa...")
         break

      #if para verificar se a op desejada é valida
      if opcao_selecionada in [1, 2, 3, 4, 5]:
         #se valida seta as opções validas       
         opcoes = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]
         while True:
            ## retorna para o menu principal se nao for a op 1 a selecionada
            if opcao_selecionada!=1:
               print("\n==========EM DESENVOLVIMENTO============\n")
               break
            # print mostrando qual o menu foi selecionado
            print(f"\n****[{opcoes[opcao_selecionada-1]}] MENU DE OPERAÇÕES*****\n")
            
            ## for para iterar sobre opcao_crud e armazenar valor em opcoes_crud
            for opcoes_crud in opcao_crud:
               print(f"| ({opcoes_crud[0]:<1})  {opcoes_crud[1]:<30} |")
            print("\n+-------------------------------------+")

            # validação para user informar ação   
            try:
               acao_desejada=int(input("Informe a ação desejada: "))
               if acao_desejada == 9:
                  break

               ## para incluir estudantes
               elif acao_desejada==1 and opcao_selecionada==1:
                  print("========== INCLUSÃO====================")
                  nome_estudante=str(input("Digite o nome do estudante: "))
                  estudantes.append(nome_estudante)
                  print("Aguarde...")
                  input("Pressione ENTER para continuar")
                  print("Solicitação de inclusão concluída com sucesso!")
                  continue

               ## demais op de inclusao
               elif acao_desejada==1 :
                  print("==========EM DESENVOLVIMENTO============")

               ## listar estudantes
               elif acao_desejada==2 and opcao_selecionada==1:
                  print("========== LISTAGEM ===================")
                  if len(estudantes)<1:
                     print("\n====Não há estudantes cadastrados===")
                  else:
                     for estudante in estudantes:
                        print(f"- {estudante}")
                        input("Pressione ENTER para continuar")
                  continue
               
               ##listar demais op
               elif acao_desejada==2:
                  print("==========EM DESENVOLVIMENTO============")

               ##atulizar
               elif acao_desejada==3:
                  print("==========EM DESENVOLVIMENTO============")
                  continue
               
               ##excluir
               elif acao_desejada==4:
                  print("==========EM DESENVOLVIMENTO============")
                  continue

               ##  caso o user digite um numero int mas que não seja valido de alguma ação
               else:
                  print("Digite um valor válido!")

            #  caso user digite uma string 
            except ValueError:
               print("Açao invalida tente novamente")

      ## caso o user digite algum numero diferente das op validas     
      else:
         print("\nOpção inválida! Tente novamente.\n")
         
## chamada da função principal  
main()