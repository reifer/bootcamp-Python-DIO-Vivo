import sqlite3
from pathlib import Path

# Definir o caminho para o arquivo do banco de dados
ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / "meu_banco.sqlite"

# Conectar ao banco de dados
conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Criar a tabela clientes se ela não existir
def criar_tabela(conexao, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome VARCHAR(100), 
        email VARCHAR(150)
    )
    """)
    conexao.commit()

# Inserir os dados na tabela clientes
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

# Atualizar os dados na tabela clientes
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

# Exemplo de uso para atualizar um registro
criar_tabela(conexao, cursor)  # Certifica-se de que a tabela existe
atualizar_registro(conexao, cursor, 'Reinaldo Junior', 'rei@gmail.com', 1)

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

# Inserir vários dados
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

# dados = [
#     ("Reinaldo Junior", "reifer@gmail.com"),
#     ("Ana Lara", "larinha@gmail.com"),
#     ("Natalia", "naty@gmail.com"),
#     ("Mirela", "mi@gmail.com"),
#     ("Junior", "juninho@gmail,com"),
# ]
# inserir_muitos(conexao, cursor, dados)

def recuperar_clientes(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()  # Adicione os parênteses para invocar o método fetchone()

cliente = recuperar_clientes(cursor, 1)
print(cliente)

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

# Fechar a conexão após o uso
conexao.close()