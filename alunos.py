import banco
import hashlib

# Registra os alunos
def registrarAluno (banco, username, nome, sobrenome, email, senha):
    cursor = banco.cursor()

    hash = hashlib.sha512(str(senha).encode("utf-8")).hexdigest()

    try:
        cursor.execute("INSERT INTO alunos (username, nome, sobrenome, email, senha) VALUES\
                        (?, ?, ?, ?, ?)", (username, nome, sobrenome, email, hash))

        banco.commit()

        criou = True

    except:
        criou = False

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

        if hashReal[0] == hash:
            return True
        return False

    except:
        # Caso não tenha encontrado o username
        return False