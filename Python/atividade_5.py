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
    digitar("const arr = [3, 9, 2, 7];"
            "Reordene os números em ordem decrescente, sem usar .sort().\n", 0.01)
    try:
        digitar("Abrindo pagina...\n", 0.09)
        time.sleep(2)
        webbrowser.open(os.path.abspath("HTML\pagina_atividade5.html"))
    except Exception as e:
        digitar(f"Erro: {e}\n")

