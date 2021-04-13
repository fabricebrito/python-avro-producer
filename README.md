# python-avro-producer

## Setup kafka

Use `docker-compose` to setup the kafka resources:

```console
docker-compose up -d
```

## Create the python environment for the tutorial

```console
mamba env create -f environment.yml
```

Activate the environment with:

```
conda activate env-kafka
```

### Produce a few messages 

```console
 python send_record.py --topic create-user-request --schema-file create-user-request.avsc --record-value '{"email": "email4@email.com", "firstName": "Jane", "lastName": "Doe"}' --record-key a-key
 python send_record.py --topic create-user-request --schema-file create-user-request.avsc --record-value '{"email": "email@email.com", "firstName": "Bob", "lastName": "Jones"}'
 python send_record.py --topic create-user-request --schema-file create-user-request.avsc --record-value '{"email": "email2@email.com", "firstName": "Jane", "lastName": "Smith"}'
```

Open the URL: http://localhost:9021/clusters/

### Consume messages

```console
python consume_record.py --topic create-user-request --schema-file create-user-request.avsc
```

### Shutdown

```console
docker-compose down
```

Prune (optional)

```console
docker system prune -a --volumes --filter "label=io.confluent.docker"
```


### Next steps: add Grafana

https://www.novatec-gmbh.de/en/blog/data-visualization-with-kafka-how-to-use-and-connect-grafana-to-your-cluster/

### Streams

```console
CREATE STREAM pageview_avro
  (firstName VARCHAR,
   email VARCHAR)
  WITH (KAFKA_TOPIC='create-user-request',
        VALUE_FORMAT='Avro');
```