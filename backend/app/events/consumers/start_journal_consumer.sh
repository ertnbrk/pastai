#!/bin/sh
# Wait for Kafka to be ready
sleep 10
# Start the journal consumer
python -u -m events.consumers.journal_consumer
