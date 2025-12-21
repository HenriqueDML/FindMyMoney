from faker import Faker
import random
fake = Faker('pt_BR')
class User():
    def __init__(self):
        self.name = fake.name() 
        self.id = fake.uuid4()
        self.birth = fake.date_of_birth(minimum_age=18, maximum_age=100)
        self.income = random.randint(1,7) #especificar qual renda entra na opções de 1 a 7
        self.email = fake.free_email()
        self.estate = fake.city()
        self.city =  fake.estado_nome()
        self.RegisterDate = fake.iso8601()
