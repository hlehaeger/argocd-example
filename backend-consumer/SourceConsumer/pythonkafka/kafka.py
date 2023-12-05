from kafka import KafkaProducer, KafkaConsumer
import json

bootstrap_servers_ip = 'kafka.application.svc.cluster.local:9092'
# Set up Kafka producer
# producer = KafkaProducer(
#     bootstrap_servers=bootstrap_servers,
#     value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#     security_protocol='SASL_PLAINTEXT',
#     sasl_plain_username='user1',
#     sasl_plain_password='1234',
#     sasl_mechanism='PLAIN'
# )

# Set up Kafka consumer
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=bootstrap_servers_ip,
    # group_id='1',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    security_protocol='SASL_PLAINTEXT',
    sasl_plain_username='user1',
    sasl_plain_password='1234',
    sasl_mechanism='PLAIN'
)
