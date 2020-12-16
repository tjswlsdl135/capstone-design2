from kafka import KafkaProducer
from kafka.errors import KafkaError
from collections import OrderedDict

import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_request_size=5242880)

file_data = OrderedDict()

file_data["text"] = "한글"
future = producer.send('testTopic', json.dumps(file_data).encode('utf-8'))

try:
    recorde_metadata = future.get(timeout=10)
except KafkaError:
    pass

