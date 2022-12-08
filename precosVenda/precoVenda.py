import sqlite3

# conecta ao banco de dados (cria o arquivo se ele ainda não existir)
conn = sqlite3.connect('precos.db')

# cria o cursor para executar os comandos SQL
cursor = conn.cursor()

# cria a tabela
cursor.execute('''
    CREATE TABLE precos (
        nome TEXT,
        preco REAL
    )
''')

# inseri alguns dados na tabela
cursor.execute('''
    INSERT INTO precos (nome, preco) VALUES
    ('Arroz', 2.99),
    ('Feijão', 3.99),
    ('Leite', 2.50)
''')

# salva as alterações no banco de dados
conn.commit()

# fecha a conexão
conn.close()
