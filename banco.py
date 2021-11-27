# Descrição: Esse arquivo possui funções necessárias para iniciar o banco
# de dados e todas as tabelas que estão contidas nele.

import sqlite3
import hashlib
from sqlite3.dbapi2 import Error

# Função para conectar com o banco de dados
def conectar ():
    banco = None

    try:
        banco = sqlite3.connect('dados.db')

        configurarTabelas (banco)

    except Error as e:
        print (e)

    return banco

# Inicia todas as tabelas do banco
def configurarTabelas (banco):
    cursor = banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS alunos (\
                    username text NOT NULL PRIMARY KEY,\
                    nome text NOT NULL,\
                    sobrenome text NOT NULL,\
                    email text NOT NULL,\
                    senha text NOT NULL)")

    banco.commit()