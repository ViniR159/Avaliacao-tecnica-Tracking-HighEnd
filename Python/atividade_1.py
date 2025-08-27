import sys, time
import sqlite3

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
            "Explique como você faria o mapeamento entre os campos recebidos e as colunas da tabela.", 0.02)

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

  conn = sqlite3.connect("clientes.db")
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS leads (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL
  )
  """)
  try:
    cursor.execute(
      "INSERT INTO leads (nome, email, phone) VALUES (?, ?, ?)",
      (nome, email, phone)
    )
    conn.commit()
    digitar(f"Usuario {nome} salvo(a) com sucesso\n", 0.01)
  except Exception as e:
    digitar(f"Erro ao salvar no banco de dados\n"
            f"Erro: {e}", 0.01)

  conn.close()
  time.sleep(2)

