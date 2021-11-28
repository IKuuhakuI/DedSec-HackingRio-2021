# Descrição: Esse arquivo contém todas as funções referentes aos
# alunos

from sqlite3.dbapi2 import Cursor, Error
import banco
import hashlib

# Registra os alunos
def registrarAluno (banco, username, nome, email, senha):
    cursor = banco.cursor()

    hash = hashlib.sha512(str(senha).encode("utf-8")).hexdigest()

    try:
        cursor.execute("INSERT INTO alunos (username, nome, email, senha) VALUES\
                        (?, ?, ?, ?)", (username, nome, email, hash))

        banco.commit()

        criou = True

    except Error as e:
        criou = False
        print ("Erro: ", e)

    # TESTES PARA VERIFICAR O ESTADO DA CRIAÇÃO #
    # cursor.execute("SELECT * FROM alunos")
    # print(cursor.fetchall())

    return criou

# Verifica se o aluno e a senha estão corretas
def validarAluno (banco, username, senha):
    cursor = banco.cursor()

    # Hash da senha
    hash = hashlib.sha512(str(senha).encode("utf-8")).hexdigest()

    # busca pelo username e valida a senha
    try:
        cursor.execute ("SELECT senha FROM alunos WHERE username = (?)", (username,))
        hashReal = cursor.fetchone()

        # Verifica os valores retornados por cada hash #
        # print (hashReal[0])
        # print (hash)

        if hashReal == None:
            return False

        if hashReal[0] == hash:
            return True
        return False

    except Error as e:
        # Caso não tenha encontrado o username
        print ("Erro: ", e)
        return False

def verificarAvatar (banco, username):
    cursor = banco.cursor()
    
    try:
        cursor.execute ("SELECT temAvatar FROM alunos WHERE username = (?)", (username,))
        temAvatar = cursor.fetchone()

        if temAvatar[0] == False:
            return False
        else:
            return True

    except Error as e:
        print ("Erro: ", e)
        return False

def confirmarAvatar (banco, username):
    cursor = banco.cursor()

    try:
        cursor.execute ("UPDATE alunos SET temAvatar = true WHERE username = (?)", (username,))
    except Error as e:
        print ("Erro: ", e)
        return False

    return True