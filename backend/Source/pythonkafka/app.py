from flask import Flask, request, jsonify
from .kafka import producer
import logging

logging.basicConfig(filename='/var/log/app.log', level=logging.DEBUG)
app = Flask(__name__)
TOPIC_NAME = 'test'
# Define a route to produce messages to Kafka
@app.route('/produce', methods=['POST'])
def produce_message():
    data = request.get_json()
    print(f"Data received: {data}")
    # Produce the message to Kafka
    future = producer.send(TOPIC_NAME, data)
    record_metadata = future.get(timeout=10)
    print(f"Message sent to topic {record_metadata.topic} partition {record_metadata.partition} with offset {record_metadata.offset}")
    return jsonify({'status': 'success', 'message': f'Message sent to {record_metadata.topic} in partition {record_metadata.partition} with offset {record_metadata.offset}'})

# # Define a route to consume messages from Kafka
# @app.route('/consume', methods=['GET'])
# def consume_message():
#     messages = []

#     # Consume messages from Kafka
#     for message in consumer:
#         messages.append(message.value)

#     return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
