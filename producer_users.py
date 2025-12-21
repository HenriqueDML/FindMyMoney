import time
import json
from Entities import User

def rodar_cadastro():
    print("Gerador de Cadastros iniciado...")
    while True:
        novo_user = User()
        dados = novo_user.para_dict()
        print(f"[CADASTRO] Novo Usuário: {novo_user.name}")

        time.sleep(5)

if __name__ == "__main__":
    rodar_cadastro()

