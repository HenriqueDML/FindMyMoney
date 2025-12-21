from faker import Faker
import random
fake = Faker('pt_BR')

class User():
    def __init__(self, name, id, birth, income, email, ZipCode, RegisterDate):
        self.name = name
        self.id = id
        self.birth = birth
        self.income = income
        self.email = email
        self.ZipCode = ZipCode
        self.RegisterDate = RegisterDate

class Transaction:
    def __init__(self, remetente_id, destinatario_id):
        self.transaction_id= fake.uuid4()
        
        self.sender_id = remetente_id
        self.receiver_id = destinatario_id

        self.amount = round(random.uniform(1.00, 10000.00), 2)
        
        self.type = random.choice(["PIX"], ["BOLETO"], ["TED"])
        self.timestamp = fake.iso8601()
        self.status = random.choice(["APROVADO"],["NEGADO"])