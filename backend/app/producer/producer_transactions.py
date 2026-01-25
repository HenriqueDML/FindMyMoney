import time
import random
from app.entities.Entities import Transaction
from app.producer.kafka_producer import enviar_evento

usuarios_ativos = ["id_fake_1", "id_fake_2", "id_fake_3"]

def rodar_transacoes():
    print("Gerador de Transacoes iniciado")
    while True:
        if not usuarios_ativos:
            continue

        remetente = random.choice(usuarios_ativos)
        nova_tx = Transaction(remetente_id=remetente)
        dados = nova_tx.para_dict()

        # DEBUG print
        print(f"[TRANSACAO] Usuário {remetente} enviou R$ {nova_tx.amount}")
        print(f"{dados}")

        # Enviar para Kafka
        enviar_evento("transactions", dados)

        time.sleep(2)

if __name__ == "__main__":
    rodar_transacoes()
