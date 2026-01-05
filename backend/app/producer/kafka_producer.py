from kafka import KafkaProducer
import json
from datetime import date

def json_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f'Tipo {type(obj)} não serializável')

# Configuração do Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # dentro do Docker Compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def enviar_evento(topic, evento):
    producer.send(topic, evento)
    print(f"[KAFKA DEBUG] Evento enviado para {topic}: {evento}")
