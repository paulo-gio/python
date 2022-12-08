import sqlite3

# conecta ao banco de dados
conn = sqlite3.connect('precos.db')

# cria o cursor
cursor = conn.cursor()

# cria a tabela preços
cursor.execute("""
CREATE TABLE preços (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preço REAL NOT NULL
);
""")

# adiciona alguns dados de teste
cursor.execute("INSERT INTO preços (nome, preço) VALUES ('Arroz', 3.45)")
cursor.execute("INSERT INTO preços (nome, preço) VALUES ('Feijão', 4.35)")
cursor.execute("INSERT INTO preços (nome, preço) VALUES ('Leite', 2.55)")

# salva as alterações
conn.commit()

# fecha a conexão
conn.close()
