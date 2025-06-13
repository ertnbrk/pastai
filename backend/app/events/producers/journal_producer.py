import json
import os
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "kafka:9092")

producer = None
try:
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER_URL],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
except NoBrokersAvailable:
    print(f"[Kafka] No brokers available at {KAFKA_BROKER_URL}. Journal events will not be published.")


def publish_journal_recorded(user_id, journal_text):
    if not producer:
        print("[Kafka] Producer not initialized. Event not sent.")
        return
    event = {
        'event_type': 'JournalRecorded',
        'user_id': user_id,
        'journal_text': journal_text
    }
    producer.send('journal_events', event)
    producer.flush()

# Example usage
# publish_journal_recorded(1, 'Today I went to the park.')