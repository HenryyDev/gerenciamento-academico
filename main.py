# Nome: Henrique Luiz Ribeiro 
# Curso: Análise e desenvolvimento de sistemas
from collections import namedtuple
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
    dados_estudantes=namedtuple('dados_estudantes',["codigo",'nome','cpf'])
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
                  codigo_estudante=int(input("Digite o codigo do estudante: "))
                  nome_estudante=str(input("Digite o nome do estudante: "))
                  cpf_estudante=str(input("Digite o cpf do estudante: "))
                  dado_estudante=dados_estudantes(codigo_estudante,nome_estudante,cpf_estudante)
                  estudantes.append(dado_estudante)
                  print("Aguarde...")
                  input("Pressione ENTER para continuar")
                  print("Solicitação de inclusão concluída com sucesso!")
                  continue

               ## listar estudantes
               elif acao_desejada == 2 and opcao_selecionada == 1:
                  print("========== LISTAGEM ===================")
                  if len(estudantes) < 1:
                      print("==== Não há estudantes cadastrados ====")
                  else:
                      print("+-------------------------------------+")
                      print("| Código   | Nome           | CPF           ")
                      print("+-------------------------------------+")
                      for estudante in estudantes:
                          print(f"| {estudante.codigo:<8} | {estudante.nome:<14} | {estudante.cpf:<12} ")
                      print("+-------------------------------------+")
                  input("Pressione ENTER para continuar")
               elif acao_desejada==3 and opcao_selecionada==1:
                  print("==========ATUALIZAR==============")
                  if len(estudantes) < 1:
                      print("==== Não há estudantes cadastrados ====")
                  else:
                     codigo_atualizar=int(input("Digite o codigo do estudante que deseja atualizar: "))
                     estudante_encontrado=None
                     for i, estudante in enumerate(estudantes):
                        if estudante.codigo==codigo_atualizar:
                           estudante_encontrado=i
                           break
                     if estudante_encontrado is not None:
                        print(f"Estudante encontrado: {estudantes[estudante_encontrado].nome}")
                        novo_nome=input("Digite o novo nome do estudante: ")
                        novo_cpf=input("Digite o novo cpf do estudante: ")
                        if novo_nome is not None and novo_cpf is not None:
                           estudantes[estudante_encontrado]=dados_estudantes(codigo=codigo_atualizar,nome=novo_nome,cpf=novo_cpf)
                           print("Dados atualizados com sucesso!")
                           input("Pressione ENTER para continuar")
                        else:
                           print("Dados inválidos!")

               elif acao_desejada==4 and opcao_selecionada==1:
                  print("==========EXCLUSÃO=======================")
                  if len(estudantes) < 1:
                      print("==== Não há estudantes cadastrados ====")
                  else:
                     codigo_atualizar=int(input("Digite o codigo do estudante que deseja excluir: "))
                     estudante_encontrado=None
                     for i, estudante in enumerate(estudantes):
                        if estudante.codigo==codigo_atualizar:
                           estudante_encontrado=i
                           break
                     if estudante_encontrado is not None:
                        print(f"Estudante encontrado: {estudantes[estudante_encontrado].nome}")
                        print("Deseja realmente excluir o estudante? (s/n)")
                        confirmacao=input("Digite a opção desejada: ")
                        if confirmacao=="s":
                           estudantes.pop(estudante_encontrado)
                           print("Estudante excluído com sucesso!")
                           input("Pressione ENTER para continuar")
                           continue
                        else:
                           print("Exclusão cancelada!")
                           input("Pressione ENTER para continuar")
                           continue
                ## demais op de inclusao
               elif acao_desejada==1 :
                  print("==========EM DESENVOLVIMENTO============")
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
         print("Opção inválida! Tente novamente.\n")
         
## chamada da função principal  
main()