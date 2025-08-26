import sys, time
import sqlite3

def digitar(questao):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def atividade1():
  
  digitar("Um cliente envia um formulário com 3 campos: nome, email e telefone. "
            "O webhook recebe os dados no seguinte formato. "
            "Queremos salvar isso em uma tabela de banco de dados chamada leads, "
            "que possui as colunas: nome, email, telefone. "
            "Explique como você faria o mapeamento entre os campos recebidos e as colunas da tabela.")

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
    print(f"Usuario {nome} salvo(a) com sucesso")
  except Exception :
    print(f"Erro ao salvar no banco de dados")

  conn.close()

