import os
import sys
import logging
import click
from .send_record import send_record


@click.command(
    short_help="Produce message",
    help="Generates a message and sends it to kafka",
)
@click.option(
    "--record-key",
    "record_key",
    required=False,
    help="Record key. If not provided, will be a random UUID",
)
@click.option("--schema-file", "schema_file", help="File name of Avro schema to use")
@click.option(
    "--record-value",
    "record_value",
    help="Record value",
)
@click.option(
    "--topic",
    "topic",
    help="Topic name",
)
@click.option(
    "--bootstrap-servers",
    "bootstrap_servers",
    required=False,
    default="localhost:9092",
    help="Bootstrap server address",
)
@click.option(
    "--schema-registry",
    "schema_registry",
    required=False,
    default="http://localhost:8081",
    help="Schema Registry url",
)
@click.pass_context
def main(ctx, **kwargs):

    send_record(**kwargs)

if __name__ == "__main__":
    main()
