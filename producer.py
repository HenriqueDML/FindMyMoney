import json
from faker import Faker
from faker.providers import internet
#from confluent_kafka import Producer

fake = Faker('PT-BR')

nome = fake.name()
address = fake.address()
provedor = fake.add_provider(internet)


print(nome)
print(address)
print(provedor)