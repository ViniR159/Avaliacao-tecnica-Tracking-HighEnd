import sys, time

def digitar(questao, vlc):
    for ch in questao:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(vlc)
    print()

lista_objs = [
    {"nome": "Maria", "idade": None, "email": "maria@teste.com"},
    {"nome": "João", "idade": 25, "email": None},
    {"nome": None, "idade": 22, "email": "Luke@teste.com"},
    {"nome": "João", "idade": 24, "email": None}
]

def atividade():
    digitar("Escreva uma função que receba um objeto e remova todas as propriedades que tenham valor null ou undefined.", 0.05)

    for obj in lista_objs:
        for chave in list(obj.keys()):
            if obj[chave] is None:
                del obj[chave]

    digitar(str(lista_objs), 0.02)