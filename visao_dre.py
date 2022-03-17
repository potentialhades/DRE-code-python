import controle_dre as cd
import time

def menu():
    try:
        cd.titulo_texto('MENU - DRE')
        print('''
              --------------------------------------
              | [1] | Gerar DRE do novo Mês        |
              |------------------------------------|
              | [2] | Inserir valores - Despesas   |
              | [3] | Mostrar Despesas do Mês      |
              |------------------------------------|
              | [4] | Inserir valores - Receitas   |
              | [5] | Mostrar Receitas do Mês      |
              |------------------------------------|
              | [6] | Calcular Totais do Mês       |
              | [7] | Comparação DRE entre 2 meses |
              |------------------------------------|
              | [0] | Fechar Menu                  |
              --------------------------------------
              \n'''+80*'-')
        opc = int(input('Digite o número opção: '))
        while opc < 0 or opc >= 8:
            print('Digite uma opção válida!\n')
            opc = int(input('Digite o número da opção: '))
        if opc == 1:
            data = cd.verifica_data()
            cd.gerar_financeiro(data)
            print('Novo DRE {} gerado com sucesso!\n'.format(data))
            time.sleep(4)
        if opc == 2:
            i = 1
            data = cd.verifica_data()
            while i != 0:
                cd.alterar_valor(1, data)
                n = int(input('Deseja alterar mais algum valor? Digite o número da opção: [0] - Não   [1] - Sim\n'))
                while n >= 3 or n < 0:
                    n = int(input('Opção inválida! Digite o número da opção: [0] - Não   [1] - Sim\n'))
                i = n
            print('--Retornando ao menu em alguns segundos--\n')
            time.sleep(4)
        if opc == 3:
            data = cd.verifica_data()
            cd.mostrar_despesas(data)
            print('--Retornando ao menu em alguns segundos--\n')
            time.sleep(5)
        if opc == 4:
            i = 1
            data = cd.verifica_data()
            while i != 0:
                cd.alterar_valor(2, data)
                n = int(input('Deseja alterar mais algum valor? Digite o número da opção: [0] - Não   [1] - Sim\n'))
                while n >= 3 or n < 0:
                    n = int(input('Opção inválida! Digite o número da opção: [0] - Não   [1] - Sim\n'))
                i = n
            print('--Retornando ao menu em alguns segundos--\n')
            time.sleep(4)
        if opc == 5:
            data = cd.verifica_data()
            cd.mostrar_receitas(data)
            print('--Retornando ao menu em alguns segundos--\n')
            time.sleep(5)
        if opc == 6:
            data = cd.verifica_data()
            cd.calcular_totais(data)
            print('\n--Retornando ao menu em alguns segundos--\n')
            time.sleep(5)
        if opc == 7:
            print('\nInsira a data referente dos meses:')
            data1 = cd.verifica_data()
            data2 = cd.verifica_data()
            cd.comparar_dre(data1, data2)
            print('\n--Retornando ao menu em alguns segundos--\n')
            time.sleep(10)
        if opc == 0:
            print('\n-- Você fechou o programa. Até logo ;) --\n')
            time.sleep(5)
            exit()
    except ValueError:
        print('Digite uma opção válida!!')