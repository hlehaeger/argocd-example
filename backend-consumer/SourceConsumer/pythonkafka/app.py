from flask import Flask, request, jsonify
from .kafka import consumer
import json
app = Flask(__name__)
TOPIC_NAME = 'test'
# Define a route to produce messages to Kafka
# @app.route('/produce', methods=['POST'])
# def produce_message():
#     data = request.get_json()
#     message = data.get('message')

#     # Produce the message to Kafka
#     producer.send(TOPIC_NAME, {'message': message})
#     return jsonify({'status': 'success', 'message': 'Message sent to Kafka'})

# # Define a route to consume messages from Kafka
@app.route('/consume', methods=['GET'])
def consume_message():
    messages = []
    consumer.subscribe([TOPIC_NAME])
    # Consume messages from Kafka
    print(f"Consumer object {vars(consumer)}")
    for message in consumer:
        # Process the received message
        print(f"Received message: {message.value}")
        messages.append(message.value)

    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
