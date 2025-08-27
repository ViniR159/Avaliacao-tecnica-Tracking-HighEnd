import sys, time

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def atividade():
    digitar("Você deve construir uma pequena API (pode ser em Node.js/Python ou dentro do n8n)\n"
    "que consuma a API pública REST Countries  e disponibilize funcionalidades de listagem, busca e avaliação de países.", 0.02)



atividade()