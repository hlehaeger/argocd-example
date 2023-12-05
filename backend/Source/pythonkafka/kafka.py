from kafka import KafkaProducer, KafkaConsumer
import json

bootstrap_servers = 'kafka.default.svc.cluster.local:9092'
# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    security_protocol='PLAINTEXT',
    sasl_plain_username='user1',
    sasl_plain_password='1234',
    sasl_mechanism='PLAIN'
)

# # Set up Kafka consumer
# consumer = KafkaConsumer(
#     'your_kafka_topic',
#     bootstrap_servers='your_kafka_bootstrap_servers',
#     group_id='your_consumer_group',
#     auto_offset_reset='earliest',
#     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
# )
