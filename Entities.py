from faker import Faker
import uuid
from datetime import datetime
import random

fake = Faker('pt_BR')

class User:
    def __init__(self):
        self.name = fake.name() 
        self.id = fake.uuid4()
        self.birth = fake.date_of_birth(minimum_age=18, maximum_age=100)
        self.income = random.randint(1,7) #especificar qual renda entra na opções de 1 a 7
        self.email = fake.free_email()
        self.estate = fake.city()
        self.city =  fake.estado_nome()
        self.RegisterDate = fake.iso8601()

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

    def para_dict(self):
        return {
            "tipo_evento": "FINANCIAL_TRANSACTION",
            "payload": self.__dict__ 
        }