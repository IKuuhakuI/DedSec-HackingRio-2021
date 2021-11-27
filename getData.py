import sqlite3

banco = sqlite3.connect('dados.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE alunos (\
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                nome text NOT NULL,\
                sobrenome text NOT NULL,\
                email text NOT NULL,\
                senha text NOT NULL)")

# cursor.execute("INSERT INTO alunos (nome, sobrenome, email, senha) VALUES ('Luiz', 'Carrion', 'teste@gmail.com', '12345')")

# cursor.execute("SELECT * FROM alunos")

# print (cursor.fetchall())

banco.commit()