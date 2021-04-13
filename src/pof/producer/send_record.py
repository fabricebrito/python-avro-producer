import json
import uuid
import logging
import sys
from confluent_kafka.avro import AvroProducer
from ..utils import load_avro_schema_from_file

logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


def send_record(kwargs):

    key_schema, value_schema = load_avro_schema_from_file(kwargs["schema_file"])

    producer_config = {
        "bootstrap.servers": kwargs["bootstrap_servers"],
        "schema.registry.url": kwargs["schema_registry"],
    }

    producer = AvroProducer(
        producer_config,
        default_key_schema=key_schema,
        default_value_schema=value_schema,
    )

    key = kwargs.get("record_key") if kwargs.get("record_key") else str(uuid.uuid4())
    value = json.loads(kwargs["record_value"])

    try:
        producer.produce(topic=kwargs["topic"], key=key, value=value)
    except Exception as e:
        logging.error(
            f"Exception while producing record value - {value} to topic - {kwargs['topic']}: {e}"
        )
    else:
        logging.info(
            f"Successfully producing record value - {value} to topic - {kwargs['topic']}"
        )

    producer.flush()
