import os
import sys
import logging
import click
from .consume_record import consume_record


@click.command(
    short_help="Consume message",
    help="Consumes a message from a topic",
)
@click.option("--schema-file", "schema_file", help="File name of Avro schema to use")
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

    consume_record(kwargs)

if __name__ == "__main__":
    main()
