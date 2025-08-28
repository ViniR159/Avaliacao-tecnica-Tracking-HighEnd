import sys, time, os, threading, webbrowser
import uvicorn
import json
from InquirerPy import inquirer
import requests
from fastapi import FastAPI, HTTPException, Query, Body

app = FastAPI()

api_paises = "https://restcountries.com/v3.1/all?fields=name,population,capital,region,languages,flags"

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

@app.get("/paises/buscar")
def buscar_pais(nome: str = Query(..., description="Nome do país a ser buscado")):
    paises = obter_paises()

    for p in paises:
        if p["name"]["common"].lower() == nome.lower():
            return {
                "nome": p["name"]["common"],
                "populacao": p.get("population", 0),
                "capital": p.get("capital", ["Desconhecida"])[0],
                "regiao": p.get("region", "Não informado"),
                "idiomas": list(p.get("languages", {}).values()),
                "bandeira": p.get("flags", {}).get("png", "")
            }

    raise HTTPException(status_code=404, detail="País não encontrado")


avaliacoes = {}

@app.post("/paises/avaliar")
def avaliar_pais(
    nome: str = Body(..., embed=True, description="Nome do país a ser avaliado"),
    curti: bool = Body(..., embed=True, description="Avaliação: True = curti, False = não curti")):

    paises = obter_paises()

    pais = next((p for p in paises if p["name"]["common"].lower() == nome.lower()), None)
    if not pais:
        raise HTTPException(status_code=404, detail="País não encontrado")

    if pais["name"]["common"] not in avaliacoes:
        avaliacoes[pais["name"]["common"]] = {"curti": 0, "nao_curti": 0}

    if curti:
        avaliacoes[pais["name"]["common"]]["curti"] += 1
    else:
        avaliacoes[pais["name"]["common"]]["nao_curti"] += 1

    total_votos = avaliacoes[pais["name"]["common"]]["curti"] + avaliacoes[pais["name"]["common"]]["nao_curti"]

    return {
        "pais": pais["name"]["common"],
        "status": "sucesso",
        "curti": avaliacoes[pais["name"]["common"]]["curti"],
        "nao_curti": avaliacoes[pais["name"]["common"]]["nao_curti"],
        "total_votos": total_votos
    }

def curtir(nome_pais: str):
    os.system("cls")
    voto = inquirer.select(
        message=f"Você curtiu {nome_pais}?",
        choices=[" Curti", " Não curti"],
    ).execute()

    curti = True if voto == " Curti" else False

    resposta = requests.post(
        "http://127.0.0.1:8000/paises/avaliar",
        json={"nome": nome_pais, "curti": curti}
    )

    if resposta.status_code == 200:
        resultado = resposta.json()
        digitar("\n Avaliação registrada com sucesso!",0.02)
        digitar(f"País: {resultado['pais']}",0.02)
        digitar(f"Curtidas: {resultado['curti']} |  Não curtidas: {resultado['nao_curti']} | Total: {resultado['total_votos']}",0.02)
    else:
        digitar("Erro ao avaliar:", resposta.text,0.02)

@app.get("/paises/curtidos")
def paises_curtidos():
    curtidos = [
        {"pais": nome, "curti": dados["curti"], "nao_curti": dados["nao_curti"], "total": dados["curti"] + dados["nao_curti"]}
        for nome, dados in avaliacoes.items()
        if dados["curti"] > 0
    ]
    return curtidos

def ver_curtidos():
    os.system("cls")
    resposta = requests.get("http://127.0.0.1:8000/paises/curtidos")

    if resposta.status_code == 200:
        paises = resposta.json()
        if not paises:
            digitar(" Nenhum país foi curtido ainda.\n", 0.02)
            return

        digitar(" Países curtidos:", 0.02)
        for p in paises:
            digitar(f"🇺🇳 {p['pais']} →  {p['curti']} |  {p['nao_curti']} | Total: {p['total']}", 0.02)
    else:
        digitar("Erro ao buscar países curtidos:", 0.02)


def exportar():
    time.sleep(5)
    os.system("cls")
    exportar = inquirer.confirm(message="Deseja exportar em Json?").execute()

    if exportar:
        digitar("Exportando...", 0.05)
        with open('Top_10_paises_populosos.json', 'w', encoding='utf-8') as f:
            json.dump(top10(), f, indent=4, ensure_ascii=False)
    else:
        os.system("cls")
        print("Processo cancelado")

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
            exportar()
        case "buscar pais":
            nome = input("Escreva o nome do pais:")
            digitar("Abrindo pagina...\n", 0.09)
            time.sleep(2)
            webbrowser.open(f"http://127.0.0.1:8000/paises/buscar?nome={nome}")
            time.sleep(1)
            curtir(nome) 
        case "ver paises já curtidos":
            ver_curtidos()
            digitar("Abrindo pagina...\n", 0.09)
            time.sleep(2)
            webbrowser.open(f"http://127.0.0.1:8000/paises/curtidos")
            time.sleep(1)


def atividade():
    os.system("cls")
    digitar("Você deve construir uma pequena API (pode ser em Node.js/Python ou dentro do n8n)\n"
    "que consuma a API pública REST Countries  e disponibilize funcionalidades de listagem, busca e avaliação de países.", 0.02)

    while True:
        escolha = inquirer.select(
            message = "escolha uma acao",
            choices = ["ver top10", "buscar pais", "ver paises já curtidos","sair"],
        ).execute()

        confirm = inquirer.confirm(message="Confirm?").execute()

        if confirm:
            if escolha == "sair":
                os.system("python ./menu.py")
            else:
                opcao_escolhida(escolha)
        else:
            os.system("cls")
            print("Processo cancelado")

if __name__ == "__main__":
    t_api = threading.Thread(target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000), daemon=True)
    t_api.start()

    time.sleep(5)
    atividade()

