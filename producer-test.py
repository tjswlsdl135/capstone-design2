from kafka import KafkaProducer
from kafka.errors import KafkaError

import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_request_size=5242880)


msg='producer test'
future = producer.send('testTopic', json.dumps(msg).encode('utf-8'))

try:
    recorde_metadata = future.get(timeout=10)
except KafkaError:
    pass

