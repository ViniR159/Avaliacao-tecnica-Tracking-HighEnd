import sys, time

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

def atividade():

    digitar("Você recebeu uma lista com 1.000 leads em JSON. "
          "A API de destino só aceita receber 100 leads por vez. "
          "Como garantir que todos os 1.000 leads sejam enviados, sem perda e sem repetição?", 0.02)
  