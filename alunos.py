import banco
import hashlib

# Registra os alunos
def registrarAluno (banco, username, nome, sobrenome, email, senha):
    cursor = banco.cursor()

    hash = hashlib.sha512(str(senha).encode("utf-8")).hexdigest()

    criou = False

    try:
        cursor.execute("INSERT INTO alunos (username, nome, sobrenome, email, senha) VALUES\
                        (?, ?, ?, ?, ?)", (username, nome, sobrenome, email, hash))

        banco.commit()

        criou = True

    except:
        print ("Username já existe!")

    cursor.execute("SELECT * FROM alunos")

    print(cursor.fetchall())

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

        print (hashReal[0])

        print (hash)

        if hashReal[0] == hash:
            return True
        return False

    except:
        return False

banco = banco.conectar()

if validarAluno (banco, "Mig", "123"):
    print ("Logado com sucesso")
else:
    print ("Usuario ou senha nao existe")
