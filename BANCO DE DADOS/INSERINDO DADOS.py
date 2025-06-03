import sqlite3

con = sqlite3.connect('banco.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    idade INTEGER
)
''')

data = ("Rafael", 32)
cursor.execute("INSERT INTO contatos (nome, idade) VALUES (?, ?)", data)
con.commit()
con.close()
