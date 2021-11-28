# Descrição: Esse arquivo possui funções necessárias para iniciar o banco
# de dados e todas as tabelas que estão contidas nele.

import sqlite3
import hashlib
from sqlite3.dbapi2 import Error

# Função para conectar com o banco de dados
def conectar ():
    banco = None

    try:
        banco = sqlite3.connect('banco/dados.db')

        configurarTabelas (banco)

    except Error as e:
        print ("Erro: ", e)

    return banco

# Inicia todas as tabelas do banco
def configurarTabelas (banco):
    cursor = banco.cursor()

    cursor.execute ("CREATE TABLE IF NOT EXISTS alunos (\
                    username text NOT NULL PRIMARY KEY,\
                    nome text NOT NULL,\
                    email text NOT NULL,\
                    senha text NOT NULL,\
                    temAvatar boolean NOT NULL DEFAULT false)")

    cursor.execute ("CREATE TABLE IF NOT EXISTS cursos (\
                    id integer NOT NULL PRIMARY KEY,\
                    nome text NOT NULL,\
                    area text NOT NULL)")

    cursor.execute ("CREATE TABLE IF NOT EXISTS perguntas (\
                    id integer NOT NULL PRIMARY KEY,\
                    )")
    banco.commit()