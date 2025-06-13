import json
from kafka import KafkaConsumer

# Initialize Kafka consumer
consumer = KafkaConsumer('journal_events',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

def process_journal_event(event):
    # Logic to process the journal event
    print(f'Processing event: {event}')

# Listen for events
for message in consumer:
    process_journal_event(message.value) 