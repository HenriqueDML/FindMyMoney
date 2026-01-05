import time
from app.entities.Entities import User
from app.producer.kafka_producer import enviar_evento

def rodar_cadastro():
    print("Gerador de Cadastros iniciado...")
    for _ in range(10):
        novo_user = User()
        dados = novo_user.para_dict()

        # DEBUG print
        print(f"[CADASTRO] Novo Usuário: {novo_user.name}, {novo_user.email}, {novo_user.birth}, {novo_user.income}, {novo_user.city}, {novo_user.estate}")

        # Enviar para Kafka
        enviar_evento("users", dados)

        time.sleep(5)

if __name__ == "__main__":
    rodar_cadastro()
