import time
import random
from Entities import Transaction

#simulacao de usuarios fakes (MUDAR DEPOIS)

usuarios_ativos = ["id_fake_1", "id_fake_2", "id_fake_3"]

def rodar_transacoes():
    print(" Gerador de Transacoes iniciado")
    while True:
        if not usuarios_ativos:
            continue

        remetente = random.choice(usuarios_ativos)

        nova_tx = Transaction(remetente_id=remetente)

        print(f"[TRANSACAO] Usuário {remetente} enviou R$ {nova_tx.amount}")

        time.sleep(2)

if __name__ == "__main__":
    rodar_transacoes()