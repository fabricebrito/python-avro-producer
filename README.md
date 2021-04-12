# python-avro-producer

## setup kafka

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

Open the URL: http://localhost:9021/clusters/Vyu6Ohb6TiuyyZz-jrF6tA/management/topics/create-user-request/message-viewer

### Consume messages

```console
python consume_record.py --topic create-user-request --schema-file create-user-request.avsc
```
