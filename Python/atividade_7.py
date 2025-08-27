import sys, time, os, threading, webbrowser
import uvicorn
from InquirerPy import inquirer
import requests
from fastapi import FastAPI, HTTPException
import webbrowser

app = FastAPI()

api_paises = "https://restcountries.com/v3.1/all?fields=name,population"

def obter_paises():
    resposta = requests.get(api_paises)
    if resposta.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao acessar API de países")
    return resposta.json()

@app.get("/paises/top10")
def top10():
    paises = obter_paises()

    paises_ordenados = sorted(paises, key=lambda x: x.get("population", 0), reverse=True)
    
    top10 = [
        {"nome": p["name"]["common"], "populacao": p.get("population", 0)}
        for p in paises_ordenados[:10]
    ]
    return top10



def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def opcao_escolhida(i):
    print(f"Opção escolhida: {i}")
    match i:
        case "ver top10":
            digitar("Abrindo pagina...\n", 0.09)
            time.sleep(2)
            webbrowser.open("http://127.0.0.1:8000/paises/top10")
            time.sleep(1)
        case "buscar pais":
            pass

def atividade():
    digitar("Você deve construir uma pequena API (pode ser em Node.js/Python ou dentro do n8n)\n"
    "que consuma a API pública REST Countries  e disponibilize funcionalidades de listagem, busca e avaliação de países.", 0.02)

    while True:
        escolha = inquirer.select(
            message = "escolha uma acao",
            choices = ["ver top10", "buscar pais"],
        ).execute()

        confirm = inquirer.confirm(message="Confirm?").execute()


        if confirm:
            opcao_escolhida(escolha)
            break
        else:
            os.system("cls")
            print("Processo cancelado")
    
def iniciarApi():
    uvicorn.run("atividade_7:app", host="127.0.0.1", port=8000)

if __name__ == "__main__":
    t = threading.Thread(target=atividade(), daemon=True)
    iniciarApi()
    t.start
