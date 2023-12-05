from flask import Flask, request, jsonify
from .kafka import consumer
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

    # Consume messages from Kafka
    for message in consumer:
        messages.append(message.value)

    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
