from faker import Faker
import uuid
from datetime import datetime
import random

fake = Faker('pt_BR')

class Transaction:
    def __init__(self, remetente_id, destinatario_id):
        #id da transacao
        self.transaction_id= str(uuid.uuid4())
        #remetente e destinatario
        self.sender_id = remetente_id
        self.receiver_id = destinatario_id
        #valor
        self.amount = round(random.uniform(1.00, 10000.00), 2)
        #Detalhamento da Transação
        self.type = random.choice(["PIX"], ["BOLETO"], ["TED"])
        self.timestamp = datetime.now().isoformat()
        self.currency = "BRL"
        self.status = random.choice(["APROVADO"],["NEGADO"])