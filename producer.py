import json
from faker import Faker
from faker.providers import internet
#from confluent_kafka import Producer

fake = Faker('PT-BR')

id_user = fake.uuid4()
nome = fake.name()
address = fake.address()
provedor = fake.add_provider(internet)

print(id_user)
print(nome)
print(address)
print(provedor)