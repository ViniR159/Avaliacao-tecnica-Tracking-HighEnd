import os
from InquirerPy import inquirer
import atividade_1, atividade_2, atividade_3, atividade_4

escolha = inquirer.select(
        message = "escolha uma opção para ver a resposta",
        choices = [1,2,3,4,5,6],
).execute()

confirm = inquirer.confirm(message="Confirm?").execute()

def opcao_escolhida(i):
    match i:
        case 1:
            print(f"Opção escolhida {i}")
            os.system("cls")
            atividade_1.atividade()
        case 2:
            print(f"Opção escolhida {i}")
            os.system("cls")
            atividade_2.atividade()
        case 3:
            print(f"Opção escolhida {i}")
            os.system("cls")
            atividade_3.atividade()
        case 4:
            print(f"Opção escolhida {i}")
            os.system("cls")
            atividade_4.atividade()
        case 5:
            print(f"Opção escolhida {i}")
        case 6:
            print(f"Opção escolhida {i}")
        case 7:
            print(f"Opção escolhida {i}")
        case _:
            print("Opção invalida")
    
if confirm:
    opcao_escolhida(escolha)
else:
    print("Até mais")