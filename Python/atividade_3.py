import sys, time, os
import json
import requests

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def grupoLeads(lista):
   for leads in range(0, len(lista), 100):
      yield lista[leads:leads+100]

def atividade():

    digitar("Você recebeu uma lista com 1.000 leads em JSON. "
          "A API de destino só aceita receber 100 leads por vez. "
          "Como garantir que todos os 1.000 leads sejam enviados, sem perda e sem repetição? \n", 0.02)
  
    api = "https://apitest007.com"

    with open("leads1000.json") as lista:
        dados = json.load(lista)

    for grupo in grupoLeads(dados):
        try:
            response = requests.post(api, json=grupo, timeout=5)
            response.raise_for_status() 
            digitar("Grupo enviado com sucesso\n", 0.01)
        except Exception as e:
            digitar(f"Erro: {e}\n", 0.01)
            
    time.sleep(5)
    os.system("python ./menu.py") 