import sqlite3

conn = sqlite3.connect('DRE.db')

def create_table_despesas():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS despesas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        valor FLOAT,
                        data_referente TEXT)''')
    except Exception as e:
        print("Erro na criação da tabela: ", e)

def create_table_receitas():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS receitas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        valor FLOAT,
                        data_referente TEXT)''')
    except Exception as e:
        print("Erro na criação da tabela: ", e)

def add_despesa(nome, valor, data_referente):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO despesas (nome, valor, data_referente) VALUES (?, ?, ?)',(nome, valor, data_referente))
        conn.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir despesa: ", e)
    finally:
        cursor.close()

def add_receita(nome, valor, data_referente):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO receitas (nome, valor, data_referente) VALUES (?, ?, ?)',(nome, valor, data_referente))
        conn.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir receita: ", e)
    finally:
        cursor.close()

def get_despesa():
    try:
        return conn.execute('SELECT id, nome, valor, data_referente FROM despesas')
    except sqlite3.Error as e:
        print("Erro ao buscar despesa: ", e)
        
def get_receita():
    try:
        return conn.execute('SELECT id, nome, valor, data_referente FROM receitas')
    except sqlite3.Error as e:
        print("Erro ao buscar receita: ", e)

def excluir_despesa(id_despesa):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM despesas WHERE id = ?',(id_despesa, ))
        conn.commit()
        conn.execute('VACUUM')
        print('Excluído com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao excluir despesa: ', e)
    finally:
        cursor.close()

def excluir_receita(id_receita):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM receitas WHERE id = ?',(id_receita, ))
        conn.commit()
        conn.execute('VACUUM')
        print('Excluído com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao excluir receita: ', e)
    finally:
        cursor.close()
        
def update_despesa(id_despesa, valor):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE despesas set valor = ? WHERE id = ?'''
        dado = (valor, id_despesa)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso!\n')
    except sqlite3.Error as e:
        print('Erro ao alterar despesa: ', e)
    finally:
        cursor.close()
        
def update_receita(id_receita, valor):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE receitas set valor = ? WHERE id = ?'''
        dado = (valor, id_receita)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso!\n')
    except sqlite3.Error as e:
        print('Erro ao alterar receita: ', e)
    finally:
        cursor.close()