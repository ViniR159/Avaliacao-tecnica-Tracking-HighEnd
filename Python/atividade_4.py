import sys, time
import os
import webbrowser

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def atividade():
    digitar("Explique a diferença entre usar == e === em JavaScript, e mostre um exemplo. \n", 0.01)
    try:
        digitar("Abrindo pagina...\n", 0.09)
        time.sleep(2)
        webbrowser.open(os.path.abspath("HTML\pagina_atividade4.html"))
    except Exception as e:
        digitar(f"Erro: {e}\n")

