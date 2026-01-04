import time
import random
from backend.app.backend.app.entities.Entities import Transaction

#simulacao de usuarios fakes (MUDAR DEPOIS)

usuarios_ativos = ["id_fake_1", "id_fake_2", "id_fake_3"]

def rodar_transacoes():
    print(" Gerador de Transacoes iniciado")
    while True:
        if not usuarios_ativos:
            continue

        remetente = random.choice(usuarios_ativos)
        
        nova_tx = Transaction(remetente_id=remetente)

        dados = nova_tx.para_dict()

        print(f"[TRANSACAO] Usuário {remetente} enviou R$ {nova_tx.amount}")
        print(f"{dados}")
        time.sleep(2)

if __name__ == "__main__":
    rodar_transacoes()