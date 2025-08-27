import sys, time
import requests


def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def atividade():
  
    digitar("Um fluxo precisa enviar os mesmos dados para 3 APIs diferentes. " 
          "Porém, se uma API falhar, o processo não pode parar "
          "— é necessário continuar tentando as outras e apenas registrar o erro ocorrido."
          "Como você estruturaria essa lógica?", 0.02
        )
  
    data = {
        "full_name": "Marcus Oliveira",
        "contact": {
        "email": "Marcus@teste.com",
        "phone": "1198989898"
        }
    }

    apisEx = {
        "https://api.com",
        "https://api1.com",
        "https://api2.com"
    }

    for api in apisEx:
        print("\n")
        try:
            response = requests.post(api, json=data, timeout=5)
            digitar(f"Dado salvo com sucesso na api {api} \n", 0.01)
        except Exception as e:
            digitar(f"Erro ao slavar na api {api}\n"
                    f"Erro: {e}\n", 0.01 )
            

