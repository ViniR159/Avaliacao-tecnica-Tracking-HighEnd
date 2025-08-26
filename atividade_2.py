import sys, time
import requests


def digitar(questao):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def atividade():
  
    digitar("Um fluxo precisa enviar os mesmos dados para 3 APIs diferentes. " 
          "Porém, se uma API falhar, o processo não pode parar "
          "— é necessário continuar tentando as outras e apenas registrar o erro ocorrido."
          "Como você estruturaria essa lógica?"
        )
  
    data = {
        "full_name": "Marcus Oliveira",
        "contact": {
        "email": "Marcus@teste.com",
        "phone": "1198989898"
        }
    }

    apisEx = {
        "https://api.com"
        "https://api1.com"
        "https://api2.com"
    }