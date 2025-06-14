import json
import os
import time
from kafka import KafkaConsumer

print("[JournalConsumer] Script started.")
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "kafka:9092")

def process_journal_event(event):
    print(f'[JournalConsumer] Processing event: {event}')

while True:
    try:
        print(f"[JournalConsumer] Connecting to Kafka at {KAFKA_BROKER_URL}...")
        consumer = KafkaConsumer(
            'journal_events',
            bootstrap_servers=[KAFKA_BROKER_URL],
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            consumer_timeout_ms=10000
        )
        print("[JournalConsumer] Connected. Listening for events...")
        for message in consumer:
            print("[JournalConsumer] Event received from Kafka queue.")
            process_journal_event(message.value)
        print("[JournalConsumer] No more events. Waiting 5 seconds...")
        time.sleep(5)
    except Exception as e:
        print(f"[JournalConsumer] Error: {e}")
        print("[JournalConsumer] Retry in 5 seconds...")
        time.sleep(5)