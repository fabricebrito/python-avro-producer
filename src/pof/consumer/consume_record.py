import sys 
import logging
from confluent_kafka.avro import AvroConsumer

logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


def consume_record(kwargs):
    default_group_name = "default-consumer-group"

    consumer_config = {
        "bootstrap.servers": kwargs["bootstrap_servers"],
        "schema.registry.url": kwargs["schema_registry"],
        "group.id": default_group_name,
        "auto.offset.reset": "earliest",
    }

    consumer = AvroConsumer(consumer_config)

    consumer.subscribe([kwargs["topic"]])

    try:
        message = consumer.poll(5)
    except Exception as e:
        print(f"Exception while trying to poll messages - {e}")
    else:
        if message:
            logging.info(
                f"Successfully poll a record from "
                f"Kafka topic: {message.topic()}, partition: {message.partition()}, offset: {message.offset()}\n"
                f"message key: {message.key()} || message value: {message.value()}"
            )
            consumer.commit()
        else:
            logging.info("No new messages at this point. Try again later.")

    consumer.close()
