import os
from InquirerPy import inquirer
from Python import atividade_1, atividade_2, atividade_3, atividade_4
from Python import atividade_5, atividade_6

def opcao_escolhida(i):
    print(f"Opção escolhida: {i}")
    match i:
        case 1:
            os.system("cls")
            atividade_1.atividade()
        case 2:
            os.system("cls")
            atividade_2.atividade()
        case 3:
            os.system("cls")
            atividade_3.atividade()
        case 4:
            os.system("cls")
            atividade_4.atividade()
        case 5:
            os.system("cls")
            atividade_5.atividade()
        case 6:
            os.system("cls")
            atividade_6.atividade()
        case 7:
            os.system("cls")
            os.system("python Python/atividade_7.py")
        case _:
            print("Opção invalida")
    
while True:
    os.system("cls")    
    escolha = inquirer.select(
            message = "escolha uma opção para ver a resposta",
            choices = [1, 2, 3, 4, 5, 6, 7],
    ).execute()

    confirm = inquirer.confirm(message="Confirm?").execute()


    if confirm:
        opcao_escolhida(escolha)
        break
    else:
        os.system("cls")
        print("Processo cancelado")
    
