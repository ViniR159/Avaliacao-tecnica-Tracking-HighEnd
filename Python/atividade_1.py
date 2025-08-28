import sys, time, os
import mysql.connector
from mysql.connector import Error

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def atividade():
    digitar("Um cliente envia um formulário com 3 campos: nome, email e telefone. "
            "O webhook recebe os dados no seguinte formato. "
            "Queremos salvar isso em uma tabela de banco de dados chamada leads, "
            "que possui as colunas: nome, email, telefone. "
            "Explique como você faria o mapeamento entre os campos recebidos e as colunas da tabela.", 0.05)

    data = {
        "full_name": "Maria Oliveira",
        "contact": {
            "email": "maria@teste.com",
            "phone": "11999998888"
        }
    }

    nome = data["full_name"]
    email = data["contact"]["email"]
    phone = data["contact"]["phone"]

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="987654",  
            database="Atividade" 
        )

        if conn.is_connected():
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL
            )
            """)

            cursor.execute(
                "INSERT INTO leads (nome, email, phone) VALUES (%s, %s, %s)",
                (nome, email, phone)
            )

            conn.commit()
            digitar(f"Usuário {nome} salvo(a) com sucesso\n", 0.01)

    except Error as e:
        digitar(f"Erro ao salvar no banco de dados\nErro: {e}", 0.01)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    time.sleep(5)
    os.system("python ./menu.py")


if __name__ == "__main__":
    atividade()
