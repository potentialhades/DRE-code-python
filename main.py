import visao_dre as vd
import banco_dre as bd

if __name__ == '__main__':
    bd.create_table_despesas()
    bd.create_table_receitas()
    while True:
        vd.menu()