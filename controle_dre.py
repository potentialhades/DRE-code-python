import banco_dre as bd
import time

def titulo_texto(texto):
    print(80*'-')
    print('\t\t\t\t',texto)
    print(80*'-')

def gerar_financeiro(data_referente):
    bd.add_despesa('DESPESAS ADMINISTRATIVAS', 0, data_referente)
    bd.add_despesa('DESPESAS COM PESSOAL', 0, data_referente)
    bd.add_despesa('DESPESAS DE COMERCIALIZAÇÃO', 0, data_referente)
    bd.add_despesa('DESPESAS TRIBUTÁRIAS', 0, data_referente)
    bd.add_despesa('DESPESAS FINANCEIRAS', 0, data_referente)
    bd.add_despesa('DESPESAS DIVERSAS', 0, data_referente)
    bd.add_despesa('DEDUÇÕES DA RECEITA', 0, data_referente)
    bd.add_despesa('COMPRAS FORNECEDOR', 0, data_referente)
    bd.add_receita('DINHEIRO', 0, data_referente)
    bd.add_receita('CARTÃO CRÉDITO', 0, data_referente)
    bd.add_receita('CARTÃO DÉBITO', 0, data_referente)
    bd.add_receita('PICPAY', 0, data_referente)
    bd.add_receita('PIX', 0, data_referente)

def mostrar_despesas(data_referente):
    titulo_texto('DESPESAS')
    for dado in bd.get_despesa():
        if data_referente == dado[3]:
            print('\nID: [{}]\t{}\tValor: R${}\tData Referente: [{}]'.format(dado[0], dado[1], dado[2], dado[3]))
    print(80*'-')

def mostrar_receitas(data_referente):
    titulo_texto('RECEITAS')
    for dado in bd.get_receita():
        if data_referente == dado[3]:
            print('\nID: [{}]\t{}\tValor: R${}\tData Referente: [{}]'.format(dado[0], dado[1], dado[2], dado[3]))
    print(80*'-')

def alterar_valor(opc, data_referente):
    try:
        if opc == 1:
            mostrar_despesas(data_referente)
            id_despesa = int(input('\nDigite o id da Despesa que deseja alterar: '))
            valor = float(input('\nDigite o novo valor: R$ '))
            bd.update_despesa(id_despesa, valor)
        if opc == 2:
            mostrar_receitas(data_referente)
            id_receita = int(input('\nDigite o id da Despesa que deseja alterar: '))
            valor = float(input('\nDigite o novo valor: R$ '))
            bd.update_receita(id_receita, valor)        
    except KeyboardInterrupt as e:
        print('\nErro na alteração: ', e)
    except ValueError as e:
        print('\nErro na alteração: [{}] -- Digite um número válido!\n'.format(e))

def calcular_totais(data_referente):
    try:
        mostrar_despesas(data_referente)
        for dado in bd.get_despesa():
            if data_referente == dado[3]:
                if dado[1] == 'DESPESAS ADMINISTRATIVAS':
                    valor1d = dado[2]
                if dado[1] == 'DESPESAS COM PESSOAL':
                    valor2d = dado[2]
                if dado[1] == 'DESPESAS DE COMERCIALIZAÇÃO':
                    valor3d = dado[2]
                if dado[1] == 'DESPESAS TRIBUTÁRIAS':
                    valor4d = dado[2]
                if dado[1] == 'DESPESAS FINANCEIRAS':
                    valor5d= dado[2]
                if dado[1] == 'DESPESAS DIVERSAS':
                    valor6d = dado[2]
                if dado[1] == 'DEDUÇÕES DA RECEITA':
                    valor7d = dado[2]
                if dado[1] == 'COMPRAS FORNECEDOR':
                    valor8d = dado[2]
        total_d = round(valor1d+valor2d+valor3d+valor4d+valor5d+valor6d+valor7d+valor8d, 2)
        print('Despesas Totais: R${}'.format(total_d))
        print(80*'-')
        time.sleep(4)
        mostrar_receitas(data_referente)
        for dado in bd.get_receita():
            if data_referente == dado[3]:
                if dado[1] == 'DINHEIRO':
                    valor1r = dado[2]
                if dado[1] == 'CARTÃO CRÉDITO':
                    valor2r = dado[2]
                if dado[1] == 'CARTÃO DÉBITO':
                    valor3r = dado[2]
                if dado[1] == 'PICPAY':
                    valor4r = dado[2]
                if dado[1] == 'PIX':
                    valor5r= dado[2]
        total_r = round(valor1r+valor2r+valor3r+valor4r+valor5r, 2)
        print('Receitas Totais: R${}'.format(total_r))
        print(80*'-')
        time.sleep(4)
        lucro = round(total_r - total_d, 2)
        margem = round((lucro/total_r)*100, 2)
        print('LUCRO: Receitas (-) Despesas = R${}'.format(lucro))
        print('MARGEM DE LUCRO: {}%'.format(margem))
        print(80*'-')
    except ZeroDivisionError:
        print('Erro no cálculo da margem: divisão por zero inválida')
    finally:
        return lucro

def comparar_dre(data_referente1, data_referente2):
    titulo_texto('DRE - {}'.format(data_referente1))
    lucro1 = calcular_totais(data_referente1)
    time.sleep(8)
    titulo_texto('DRE - {}'.format(data_referente2))
    lucro2 = calcular_totais(data_referente2)
    diferenca = round(lucro1-lucro2, 2)
    print(80*'-')
    print('Comparando os meses referentes, a diferença de lucro foi de R${}'.format(diferenca))
    if diferenca < 0:
        print('Resultado Negativo -> mês {} obteve um lucro maior comparado ao mês {}'.format(data_referente2,data_referente1))
    if diferenca > 0:
        print('Resultado Positivo -> mês {} obteve um lucro maior comparado ao mês {}'.format(data_referente1,data_referente2))
    print(80*'-')

def verifica_data():
    try:
        data = input('Digite o ano/mês referente seguindo o exemplo ao lado -> 2021-08:\n')
        r = data.find('-')
        s = data.split('-')
        ano = int(s[0])
        mes = int(s[1])
        while r != 4 or ano < 2021 or mes <= 0 or mes >= 13:
            data = input('O ano/mês não é válido! Exemplo -> 2021-12\n')
            r = data.find('-')
            s = data.split('-')
            ano = s[0]
            mes = s[1]
    except KeyboardInterrupt as e:
        print('Erro na data informada: [{}] -- Digite um ano/mês válido!\n'.format(e))
        verifica_data()
    finally:
        return data