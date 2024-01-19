from flask import Flask, request, jsonify
from bson import json_util
from .kafka import consumer
from kafka.errors import KafkaError
from threading import Thread
from pymongo import MongoClient
import json
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
TOPIC_NAME = 'test'
class BreakIt(Exception): pass

# Set up MongoDB client
client = MongoClient('mongodb://user:randompwd@mongo-app-mongodb:27017/mydatabase')
db = client.get_default_database()
collection = db['messages']

# Define a route to produce messages to Kafka
# @app.route('/produce', methods=['POST'])
# def produce_message():
#     data = request.get_json()
#     message = data.get('message')

#     # Produce the message to Kafka
#     producer.send(TOPIC_NAME, {'message': message})
#     return jsonify({'status': 'success', 'message': 'Message sent to Kafka'})

# # Define a route to consume messages from Kafka
# @app.route('/consume', methods=['GET'])
# def consume_message():
#     messages = []
#     consumer.subscribe([TOPIC_NAME])
#     # Consume messages from Kafka
#     try:
#         while True:
#                 message = consumer.poll(timeout_ms=5000)  # Wait for 5 seconds
#                 if message is None:
#                     # No message received within timeout
#                     break
#                 else:
#                     # Process the received message
#                     for tp, msgs in message.items():
#                         for msg in msgs:
#                             print(f"Received message: {msg.value}")
#                             messages.append(msg.value)
#                             raise BreakIt
#     except KafkaTimeoutError as e:
#         print(f"Exception occurred while consuming messages: {e}")
#         return jsonify({'error': f'Exception occurred while consuming messages: str{e}'})       
#     except BreakIt:
#         pass
#     return jsonify({'messages': [str(m) for m in messages]})

# Kafka consumer function
def kafka_consumer():
    consumer.subscribe([TOPIC_NAME])
    try:
        while True:
            message = consumer.poll(timeout_ms=5000)  # Wait for 5 seconds
            if message is not None:
                for tp, msgs in message.items():
                    for msg in msgs:
                        print(f"Received message: {msg.value}")
                        # Save message to MongoDB
                        collection.insert_one(msg.value)
    except KafkaError as e:
        print(f"Exception occurred while consuming messages: {e}")

# Start Kafka consumer in a background thread
consumer_thread = Thread(target=kafka_consumer)
consumer_thread.start()

@app.route('/consume', methods=['GET'])
def consume_message():
    # Get the last 10 messages from MongoDB
    messages = list(collection.find().sort('_id', -1).limit(10))
    messages_json = json.dumps(messages, default=json_util.default)
    logging.info(f"Messages: {messages_json}")
    return jsonify({'messages': messages_json})

if __name__ == '__main__':
    app.run(debug=True)
